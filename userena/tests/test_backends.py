from django.contrib.auth import get_user_model
from django.test import TestCase

from userena.backends import UserenaAuthenticationBackend

User = get_user_model()


class UserenaAuthenticationBackendTests(TestCase):
    """
    Test the ``UserenaAuthenticationBackend`` which should return a ``User``
    when supplied with a username/email and a correct password.

    """

    fixtures = ["users"]
    backend = UserenaAuthenticationBackend()

    def test_with_username(self):
        """Test the backend when usernames are supplied."""
        # Invalid usernames or passwords
        invalid_data_dicts = [
            # Invalid password
            {"identification": "john", "password": "inhalefish"},
            # Invalid username
            {"identification": "alice", "password": "blowfish"},
        ]
        for invalid_dict in invalid_data_dicts:
            result = self.backend.authenticate(
                request=None,
                identification=invalid_dict["identification"],
                password=invalid_dict["password"],
            )
            self.assertFalse(isinstance(result, User))

        # Valid username and password
        result = self.backend.authenticate(
            request=None, identification="john", password="blowfish"
        )
        self.assertTrue(isinstance(result, User))

    def test_with_email(self):
        """Test the backend when email address is supplied"""
        # Invalid e-mail adressses or passwords
        invalid_data_dicts = [
            # Invalid password
            {"identification": "john@example.com", "password": "inhalefish"},
            # Invalid e-mail address
            {"identification": "alice@example.com", "password": "blowfish"},
        ]
        for invalid_dict in invalid_data_dicts:
            result = self.backend.authenticate(
                request=None,
                identification=invalid_dict["identification"],
                password=invalid_dict["password"],
            )
            self.assertFalse(isinstance(result, User))

        # Valid e-email address and password
        result = self.backend.authenticate(
            request=None,
            identification="john@example.com",
            password="blowfish",
        )
        self.assertTrue(isinstance(result, User))

    def test_get_user(self):
        """Test that the user is returned"""
        user = self.backend.get_user(1)
        self.assertEqual(user.username, "john")

        # None should be returned when false id.
        user = self.backend.get_user(99)
        self.assertFalse(user)
