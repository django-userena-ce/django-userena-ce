import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management import call_command
from django.test import TestCase
from guardian.models import UserObjectPermission

from userena import settings as userena_settings
from userena.managers import ASSIGNED_PERMISSIONS
from userena.models import UserenaSignup
from userena.utils import get_profile_model

User = get_user_model()


class CleanExpiredTests(TestCase):
    user_info = {
        "username": "alice",
        "password": "swordfish",
        "email": "alice@example.com",
    }

    def test_clean_expired(self):
        """
        Test if ``clean_expired`` deletes all users which ``activation_key``
        is expired.

        """
        # Create an account which is expired.
        user = UserenaSignup.objects.create_user(**self.user_info)
        user.date_joined -= datetime.timedelta(
            days=userena_settings.USERENA_ACTIVATION_DAYS + 1
        )
        user.save()

        # There should be one account now
        User.objects.get(username=self.user_info["username"])

        # Clean it.
        call_command("clean_expired")

        self.assertEqual(
            User.objects.filter(username=self.user_info["username"]).count(), 0
        )


class CheckPermissionTests(TestCase):
    user_info = {
        "username": "alice",
        "password": "swordfish",
        "email": "alice@example.com",
    }

    def test_check_permissions(self):
        # Create a new account.
        user = UserenaSignup.objects.create_user(**self.user_info)
        user.save()

        # Remove all permissions
        UserObjectPermission.objects.filter(user=user).delete()
        self.assertEqual(
            UserObjectPermission.objects.filter(user=user).count(), 0
        )

        # Check it
        call_command("check_permissions")

        # User should have all permissions again
        user_permissions = UserObjectPermission.objects.filter(
            user=user
        ).values_list("permission__codename", flat=True)

        required_permissions = [
            "change_user",
            "delete_user",
            "change_profile",
            "view_profile",
        ]
        for perm in required_permissions:
            if perm not in user_permissions:
                self.fail()

        # Check it again should do nothing
        call_command("check_permissions", test=True)

    def test_incomplete_permissions(self):  # noqa:C901
        # Delete the neccesary permissions
        profile_model_obj = get_profile_model()
        content_type_profile = ContentType.objects.get_for_model(
            profile_model_obj
        )
        content_type_user = ContentType.objects.get_for_model(User)
        for model, perms in ASSIGNED_PERMISSIONS.items():
            if model == "profile":
                content_type = content_type_profile
            else:
                content_type = content_type_user
            for perm in perms:
                Permission.objects.get(
                    name=perm[1], content_type=content_type
                ).delete()

        # Check if they are they are back
        for model, perms in ASSIGNED_PERMISSIONS.items():
            if model == "profile":
                content_type = content_type_profile
            else:
                content_type = content_type_user
            for perm in perms:
                try:
                    perm = Permission.objects.get(
                        name=perm[1], content_type=content_type
                    )
                except Permission.DoesNotExist:
                    pass
                else:
                    self.fail("Found %s: " % perm)

        # Repair them
        call_command("check_permissions", test=True)

        # Check if they are they are back
        for model, perms in ASSIGNED_PERMISSIONS.items():
            if model == "profile":
                content_type = content_type_profile
            else:
                content_type = content_type_user
            for perm in perms:
                try:
                    perm = Permission.objects.get(
                        name=perm[1], content_type=content_type
                    )
                except Permission.DoesNotExist:
                    self.fail()

    def test_no_profile(self):
        """Check for warning when there is no profile"""
        # TODO: Dirty! Currently we check for the warning by getting a 100%
        # test coverage, meaning that it dit output some warning.
        user = UserenaSignup.objects.create_user(**self.user_info)

        # remove the profile of this user
        get_profile_model().objects.get(user=user).delete()

        # run the command to check for the warning.
        call_command("check_permissions", test=True)
