from django.test import TestCase
try:
    # django.VERSION < 2.0
    from django.core.urlresolvers import reverse
except ImportError:
    from django.urls import reverse


class DecoratorTests(TestCase):
    """ Test the decorators """

    def test_secure_required(self):
        """
        Test that the ``secure_required`` decorator does a permanent redirect
        to a secured page.

        """
        with self.settings(USERENA_USE_HTTPS=True):
            response = self.client.get(reverse('userena_signin'))

            # Test for the permanent redirect
            self.assertEqual(response.status_code, 301)

            # Test if the redirected url contains 'https'. Couldn't use
            # ``assertRedirects`` here because the redirected to page is
            # non-existant.
            self.assertTrue('https' in response.get('Location'))
