from django.contrib.auth import get_user_model
from django.test import TestCase

from userena.contrib.umessages.models import (
    Message,
    MessageContact,
    MessageRecipient,
)

User = get_user_model()


class MessageManagerTests(TestCase):
    fixtures = ["users", "messages"]

    def test_get_conversation(self):
        """Test that the conversation is returned between two users"""
        user_1 = User.objects.get(pk=1)
        user_2 = User.objects.get(pk=2)

        Message.objects.get_conversation_between(user_1, user_2)


class MessageRecipientManagerTest(TestCase):
    fixtures = ["users", "messages"]

    def test_count_unread_messages_for(self):
        """Test the unread messages count for user"""
        jane = User.objects.get(pk=2)

        # Jane has one unread message from john
        unread_messages = MessageRecipient.objects.count_unread_messages_for(
            jane
        )

        self.assertEqual(unread_messages, 1)

    def test_count_unread_messages_between(self):
        """Test the unread messages count between two users"""
        john = User.objects.get(pk=1)
        jane = User.objects.get(pk=2)

        # Jane should have one unread message from john
        unread_messages = (
            MessageRecipient.objects.count_unread_messages_between(jane, john)
        )

        self.assertEqual(unread_messages, 1)


class MessageContactManagerTest(TestCase):
    fixtures = ["users", "messages"]

    def test_get_contacts_for(self):
        """Test if the correct contacts are returned"""
        john = User.objects.get(pk=1)
        contacts = MessageContact.objects.get_contacts_for(john)

        # There is only one contact for John, and that's Jane.
        self.assertEqual(len(contacts), 1)

        jane = User.objects.get(pk=2)
        self.assertEqual(contacts[0].um_to_user, jane)
