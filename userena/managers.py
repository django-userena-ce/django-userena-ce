from django.db import models
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model
from django.contrib.auth.models import UserManager, Permission, AnonymousUser
from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import smart_str
from django.utils.translation import gettext as _
from django.conf import settings

from userena import settings as userena_settings
from userena.utils import (
    generate_nonce,
    get_profile_model,
    get_datetime_now,
    get_user_profile,
)
from userena import signals as userena_signals

from guardian.shortcuts import assign_perm, get_perms


import re

NONCE_RE = re.compile(r"^[\w]{40}$")

ASSIGNED_PERMISSIONS = {
    "profile": (
        ("view_profile", "Can view profile"),
        ("change_profile", "Can change profile"),
        ("delete_profile", "Can delete profile"),
    ),
    "user": (("change_user", "Can change user"), ("delete_user", "Can delete user")),
}


class UserenaManager(UserManager):
    """ Extra functionality for the Userena model. """

    def create_user(self, username, email, password, active=False, send_email=True):
        """
        A simple wrapper that creates a new :class:`User`.

        :param username:
            String containing the username of the new user.

        :param email:
            String containing the email address of the new user.

        :param password:
            String containing the password for the new user.

        :param active:
            Boolean that defines if the user requires activation by clicking
            on a link in an e-mail. Defaults to ``False``.

        :param send_email:
            Boolean that defines if the user should be sent an email. You could
            set this to ``False`` when you want to create a user in your own
            code, but don't want the user to activate through email.

        :return: :class:`User` instance representing the new user.

        """

        new_user = get_user_model().objects.create_user(username, email, password)
        new_user.is_active = active
        new_user.save()

        # Give permissions to view and change profile
        for perm in ASSIGNED_PERMISSIONS["profile"]:
            assign_perm(perm[0], new_user, get_user_profile(user=new_user))

        # Give permissions to view and change itself
        for perm in ASSIGNED_PERMISSIONS["user"]:
            assign_perm(perm[0], new_user, new_user)

        userena_profile = self.create_userena_profile(new_user)

        if send_email:
            userena_profile.send_activation_email()

        return new_user

    def create_userena_profile(self, user):
        """
        Creates an :class:`UserenaSignup` instance for this user.

        :param user:
            Django :class:`User` instance.

        :return: The newly created :class:`UserenaSignup` instance.

        """
        if isinstance(user.username, str):
            user.username = smart_str(user.username)

        try:
            profile = self.get(user=user)
        except self.model.DoesNotExist:
            profile = self.create(user=user, activation_key=generate_nonce())
        return profile

    def reissue_activation(self, activation_key):
        """
        Creates a new ``activation_key`` resetting activation timeframe when
        users let the previous key expire.

        :param activation_key:
            String containing the secret nonce activation key.

        """
        try:
            userena = self.get(activation_key=activation_key)
        except self.model.DoesNotExist:
            return False
        try:
            userena.activation_key = generate_nonce()
            userena.save(using=self._db)
            userena.user.date_joined = get_datetime_now()
            userena.user.save(using=self._db)
            userena.send_activation_email()
            return True
        except Exception:
            return False

    def activate_user(self, activation_key):
        """
        Activate an :class:`User` by supplying a valid ``activation_key``.

        If the key is valid and an user is found, activates the user and
        return it. Also sends the ``activation_complete`` signal.

        :param activation_key:
            String containing the secret nonce for a valid activation.

        :return:
            The newly activated :class:`User` or ``False`` if not successful.

        """
        if NONCE_RE.search(activation_key):
            try:
                userena = self.get(activation_key=activation_key)
            except self.model.DoesNotExist:
                return False
            if not userena.activation_key_expired():
                userena.activation_key = userena_settings.USERENA_ACTIVATED
                user = userena.user
                user.is_active = True
                userena.save(using=self._db)
                user.save(using=self._db)

                # Send the activation_complete signal
                userena_signals.activation_complete.send(sender=None, user=user)

                return user
        return False

    def check_expired_activation(self, activation_key):
        """
        Check if ``activation_key`` is still valid.

        Raises a ``self.model.DoesNotExist`` exception if key is not present or
         ``activation_key`` is not a valid string

        :param activation_key:
            String containing the secret nonce for a valid activation.

        :return:
            True if the ket has expired, False if still valid.

        """
        if NONCE_RE.search(activation_key):
            userena = self.get(activation_key=activation_key)
            return userena.activation_key_expired()
        raise self.model.DoesNotExist

    def confirm_email(self, confirmation_key):
        """
        Confirm an email address by checking a ``confirmation_key``.

        A valid ``confirmation_key`` will set the newly wanted e-mail
        address as the current e-mail address. Returns the user after
        success or ``False`` when the confirmation key is
        invalid. Also sends the ``confirmation_complete`` signal.

        :param confirmation_key:
            String containing the secret nonce that is used for verification.

        :return:
            The verified :class:`User` or ``False`` if not successful.

        """
        if NONCE_RE.search(confirmation_key):
            try:
                userena = self.get(
                    email_confirmation_key=confirmation_key,
                    email_unconfirmed__isnull=False,
                )
            except self.model.DoesNotExist:
                return False
            else:
                user = userena.user
                old_email = user.email
                user.email = userena.email_unconfirmed
                userena.email_unconfirmed, userena.email_confirmation_key = "", ""
                userena.save(using=self._db)
                user.save(using=self._db)

                # Send the confirmation_complete signal
                userena_signals.confirmation_complete.send(
                    sender=None, user=user, old_email=old_email
                )

                return user
        return False

    def delete_expired_users(self):
        """
        Checks for expired users and delete's the ``User`` associated with
        it. Skips if the user ``is_staff``.

        :return: A list containing the deleted users.

        """
        deleted_users = []
        for user in get_user_model().objects.filter(is_staff=False, is_active=False):
            if user.userena_signup.activation_key_expired():
                deleted_users.append(user)
                user.delete()
        return deleted_users

    def check_permissions(self):
        """
        Checks that all permissions are set correctly for the users.

        :return: A set of users whose permissions was wrong.

        """
        # Variable to supply some feedback
        changed_permissions = []
        changed_users = []
        warnings = []

        # Check that all the permissions are available.
        for model, perms in ASSIGNED_PERMISSIONS.items():
            if model == "profile":
                model_obj = get_profile_model()
            else:
                model_obj = get_user_model()

            model_content_type = ContentType.objects.get_for_model(model_obj)

            for perm in perms:
                try:
                    Permission.objects.get(
                        codename=perm[0], content_type=model_content_type
                    )
                except Permission.DoesNotExist:
                    changed_permissions.append(perm[1])
                    Permission.objects.create(
                        name=perm[1], codename=perm[0], content_type=model_content_type
                    )

        # it is safe to rely on settings.ANONYMOUS_USER_NAME since it is a
        # requirement of django-guardian
        for user in get_user_model().objects.exclude(
            username=settings.ANONYMOUS_USER_NAME
        ):
            try:
                user_profile = get_user_profile(user=user)
            except ObjectDoesNotExist:
                warnings.append(
                    _("No profile found for %(username)s") % {"username": user.username}
                )
            else:
                all_permissions = get_perms(user, user_profile) + get_perms(user, user)

                for model, perms in ASSIGNED_PERMISSIONS.items():
                    if model == "profile":
                        perm_object = get_user_profile(user=user)
                    else:
                        perm_object = user

                    for perm in perms:
                        if perm[0] not in all_permissions:
                            assign_perm(perm[0], user, perm_object)
                            changed_users.append(user)

        return (changed_permissions, changed_users, warnings)


class UserenaBaseProfileManager(models.Manager):
    """ Manager for :class:`UserenaProfile` """

    def get_visible_profiles(self, user=None):
        """
        Returns all the visible profiles available to this user.

        For now keeps it simple by just applying the cases when a user is not
        active, a user has it's profile closed to everyone or a user only
        allows registered users to view their profile.

        :param user:
            A Django :class:`User` instance.

        :return:
            All profiles that are visible to this user.

        """
        profiles = self.all()

        filter_kwargs = {"user__is_active": True}

        profiles = profiles.filter(**filter_kwargs)
        if user and isinstance(user, AnonymousUser):
            profiles = profiles.exclude(Q(privacy="closed") | Q(privacy="registered"))
        else:
            profiles = profiles.exclude(Q(privacy="closed"))
        return profiles
