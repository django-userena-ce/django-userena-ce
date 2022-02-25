import datetime

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.sites import shortcuts
from django.db import models
from django.utils.translation import gettext_lazy as _
from easy_thumbnails.fields import ThumbnailerImageField
from guardian.shortcuts import get_perms

from userena import settings as userena_settings
from userena.mail import UserenaConfirmationMail
from userena.managers import UserenaBaseProfileManager, UserenaManager
from userena.utils import (
    generate_nonce,
    get_datetime_now,
    get_gravatar,
    get_protocol,
    user_model_label,
)

PROFILE_PERMISSIONS = (("view_profile", "Can view profile"),)


def upload_to_mugshot(instance, filename):
    """
    Uploads a mugshot for a user to the ``USERENA_MUGSHOT_PATH`` and saving it
    under unique hash for the image. This is for privacy reasons so others
    can't just browse through the mugshot directory.

    """
    extension = filename.split(".")[-1].lower()
    path = userena_settings.USERENA_MUGSHOT_PATH % {
        "username": instance.user.username,
        "id": instance.user.id,
        "date": instance.user.date_joined,
        "date_now": get_datetime_now().date(),
    }
    return "{path}{hash}.{extension}".format(
        path=path,
        hash=generate_nonce()[:10],
        extension=extension,
    )


class UserenaSignup(models.Model):
    """
    Userena model which stores all the necessary information to have a full
    functional user implementation on your Django website.

    """

    user = models.OneToOneField(
        user_model_label,
        verbose_name=_("user"),
        related_name="userena_signup",
        on_delete=models.CASCADE,
    )

    last_active = models.DateTimeField(
        _("last active"),
        blank=True,
        null=True,
        help_text=_("The last date that the user was active."),
    )

    activation_key = models.CharField(
        _("activation key"), max_length=40, blank=True
    )

    activation_notification_send = models.BooleanField(
        _("notification send"),
        default=False,
        help_text=_(
            "Designates whether this user has already got a "
            "notification about activating their account."
        ),
    )

    email_unconfirmed = models.EmailField(
        _("unconfirmed email address"),
        blank=True,
        help_text=_(
            "Temporary email address when the user requests an email change."
        ),
    )

    email_confirmation_key = models.CharField(
        _("unconfirmed email verification key"), max_length=40, blank=True
    )

    email_confirmation_key_created = models.DateTimeField(
        _("creation date of email confirmation key"), blank=True, null=True
    )

    objects = UserenaManager()

    class Meta:
        verbose_name = _("userena registration")
        verbose_name_plural = _("userena registrations")

    def __str__(self):
        return "%s" % self.user.username

    def change_email(self, email):
        """
        Changes the email address for a user.

        A user needs to verify this new email address before it becomes
        active. By storing the new email address in a temporary field --
        ``temporary_email`` -- we are able to set this email address after the
        user has verified it by clicking on the verification URI in the email.
        This email gets send out by ``send_verification_email``.

        :param email:
            The new email address that the user wants to use.

        """
        self.email_unconfirmed = email

        self.email_confirmation_key = generate_nonce()
        self.email_confirmation_key_created = get_datetime_now()
        self.save()

        # Send email for activation
        self.send_confirmation_email()

    def send_confirmation_email(self):
        """
        Sends an email to confirm the new email address.

        This method sends out two emails. One to the new email address that
        contains the ``email_confirmation_key`` which is used to verify this
        this email address with :func:`UserenaUser.objects.confirm_email`.

        The other email is to the old email address to let the user know that
        a request is made to change this email address.

        """
        context = {
            "user": self.user,
            "without_usernames": userena_settings.USERENA_WITHOUT_USERNAMES,
            "new_email": self.email_unconfirmed,
            "protocol": get_protocol(),
            "confirmation_key": self.email_confirmation_key,
            "site": shortcuts.get_current_site(request=None),
        }

        mailer = UserenaConfirmationMail(context=context)
        mailer.generate_mail("confirmation", "_old")

        if self.user.email:
            mailer.send_mail(self.user.email)

        mailer.generate_mail("confirmation", "_new")
        mailer.send_mail(self.email_unconfirmed)

    @property
    def activation_completed(self):
        return self.activation_key == userena_settings.USERENA_ACTIVATED

    def activation_key_expired(self):
        """
        Checks if activation key is expired.

        Returns ``True`` when the ``activation_key`` of the user is expired and
        ``False`` if the key is still valid.

        The key is expired when it's set to the value defined in
        ``USERENA_ACTIVATED`` or ``activation_key_created`` is beyond the
        amount of days defined in ``USERENA_ACTIVATION_DAYS``.

        """
        expiration_days = datetime.timedelta(
            days=userena_settings.USERENA_ACTIVATION_DAYS
        )
        expiration_date = self.user.date_joined + expiration_days
        if self.activation_completed or (
            get_datetime_now() >= expiration_date
        ):
            return True
        return False

    def send_activation_email(self):
        """
        Sends a activation email to the user.

        This email is send when the user wants to activate their newly created
        user.

        """
        context = {
            "user": self.user,
            "without_usernames": userena_settings.USERENA_WITHOUT_USERNAMES,
            "protocol": get_protocol(),
            "activation_days": userena_settings.USERENA_ACTIVATION_DAYS,
            "activation_key": self.activation_key,
            "site": shortcuts.get_current_site(request=None),
        }

        mailer = UserenaConfirmationMail(context=context)
        mailer.generate_mail("activation")
        mailer.send_mail(self.user.email)


class UserenaBaseProfile(models.Model):
    """Base model needed for extra profile functionality"""

    PRIVACY_CHOICES = (
        ("open", _("Open")),
        ("registered", _("Registered")),
        ("closed", _("Closed")),
    )

    MUGSHOT_SETTINGS = {
        "size": (
            userena_settings.USERENA_MUGSHOT_SIZE,
            userena_settings.USERENA_MUGSHOT_SIZE,
        ),
        "crop": userena_settings.USERENA_MUGSHOT_CROP_TYPE,
    }

    mugshot = ThumbnailerImageField(
        _("mugshot"),
        blank=True,
        upload_to=upload_to_mugshot,
        resize_source=MUGSHOT_SETTINGS,
        help_text=_("A personal image displayed in your profile."),
    )

    privacy = models.CharField(
        _("privacy"),
        max_length=15,
        choices=PRIVACY_CHOICES,
        default=userena_settings.USERENA_DEFAULT_PRIVACY,
        help_text=_("Designates who can view your profile."),
    )

    objects = UserenaBaseProfileManager()

    class Meta:
        """
        Meta options making the model abstract and defining permissions.

        The model is ``abstract`` because it only supplies basic functionality
        to a more custom defined model that extends it. This way there is not
        another join needed.

        We also define custom permissions because we don't know how the model
        that extends this one is going to be called. So we don't know what
        permissions to check. For ex. if the user defines a profile model that
        is called ``MyProfile``, than the permissions would be
        ``add_myprofile`` etc. We want to be able to always check
        ``add_profile``, ``change_profile`` etc.

        """

        abstract = True
        default_permissions = ("add", "change", "delete")
        permissions = PROFILE_PERMISSIONS

    def __str__(self):
        return f"Profile of {self.user.username}"

    def get_mugshot_url(self):
        """
        Returns the image containing the mugshot for the user.

        The mugshot can be a uploaded image or a Gravatar.

        Gravatar functionality will only be used when
        ``USERENA_MUGSHOT_GRAVATAR`` is set to ``True``.

        :return:
            ``None`` when Gravatar is not used and no default image is supplied
            by ``USERENA_MUGSHOT_DEFAULT``.

        """
        # First check for a mugshot and if any return that.
        if self.mugshot:
            return self.mugshot.url

        # Use Gravatar if the user wants to.
        if userena_settings.USERENA_MUGSHOT_GRAVATAR:
            return get_gravatar(
                self.user.email,
                userena_settings.USERENA_MUGSHOT_SIZE,
                userena_settings.USERENA_MUGSHOT_DEFAULT,
            )

        # Gravatar not used, check for a default image.
        else:
            if userena_settings.USERENA_MUGSHOT_DEFAULT not in [
                "404",
                "mm",
                "identicon",
                "monsterid",
                "wavatar",
            ]:
                return userena_settings.USERENA_MUGSHOT_DEFAULT
            else:
                return None

    def get_full_name_or_username(self):
        """
        Returns the full name of the user, or if none is supplied will return
        the username.

        Also looks at ``USERENA_WITHOUT_USERNAMES`` settings to define if it
        should return the username or email address when the full name is not
        supplied.

        :return:
            ``String`` containing the full name of the user. If no name is
            supplied it will return the username or email address depending on
            the ``USERENA_WITHOUT_USERNAMES`` setting.

        """
        user = self.user
        if user.first_name or user.last_name:
            # We will return this as translated string. Maybe there are some
            # countries that first display the last name.
            name = _("%(first_name)s %(last_name)s") % {
                "first_name": user.first_name,
                "last_name": user.last_name,
            }
        else:
            # Fallback to the username if usernames are used
            if not userena_settings.USERENA_WITHOUT_USERNAMES:
                name = f"{user.username}"
            else:
                name = f"{user.email}"
        return name.strip()

    def can_view_profile(self, user):
        """
        Can the :class:`User` view this profile?

        Returns a boolean if a user has the rights to view the profile of this
        user.

        Users are divided into four groups:

            ``Open``
                Everyone can view your profile

            ``Closed``
                Nobody can view your profile.

            ``Registered``
                Users that are registered on the website and signed
                in only.

            ``Admin``
                Special cases like superadmin and the owner of the profile.

        Through the ``privacy`` field a owner of an profile can define what
        they want to show to whom.

        :param user:
            A Django :class:`User` instance.

        """
        # Simple cases first, we don't want to waste CPU and DB hits.
        # Everyone.
        if self.privacy == "open":
            return True
        # Registered users.
        elif self.privacy == "registered" and isinstance(
            user, get_user_model()
        ):
            return True

        # Checks done by guardian for owner and admins.
        elif "view_profile" in get_perms(user, self):
            return True

        # Fallback to closed profile.
        return False


class UserenaLanguageBaseProfile(UserenaBaseProfile):
    """
    Extends the :class:`UserenaBaseProfile` with a language choice.

    Use this model in combination with ``UserenaLocaleMiddleware`` automatically
    set the language of users when they are signed in.
    """

    # Max length is 8 to support language identifiers according to BCP47
    # https://tools.ietf.org/html/bcp47
    # The language identifier is of the form lll-Ssss
    #  - lll the language (shortest ISO 639 code, 3 letters max)
    #  - a hyphen
    #  - Ssss the script (ISO 15924 code, 4 letters)
    language = models.CharField(
        _("language"),
        max_length=8,
        choices=settings.LANGUAGES,
        default=settings.LANGUAGE_CODE[:2],
        help_text=_("Default language."),
    )

    class Meta:
        abstract = True
        default_permissions = ("add", "change", "delete")
        permissions = PROFILE_PERMISSIONS
