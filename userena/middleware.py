from django.utils import translation
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    # django.VERSION < 1.10
    MiddlewareMixin = object

from userena import settings as userena_settings
from userena.compat import SiteProfileNotAvailable
from userena.utils import get_user_profile


class UserenaLocaleMiddleware(MiddlewareMixin):
    """
    Set the language by looking at the language setting in the profile.

    It doesn't override the cookie that is set by Django so a user can still
    switch languages depending if the cookie is set.

    """
    def process_request(self, request):
        lang_cookie = request.session.get(settings.LANGUAGE_COOKIE_NAME)
        if not lang_cookie:

            try:
                # django.VERSION < 1.11
                authenticated = request.user.is_authenticated()
            except TypeError:
                authenticated = request.user.is_authenticated

            if authenticated:
                try:
                    profile = get_user_profile(user=request.user)
                except (ObjectDoesNotExist, SiteProfileNotAvailable):
                    profile = False

                if profile:
                    try:
                        lang = getattr(profile, userena_settings.USERENA_LANGUAGE_FIELD)
                        translation.activate(lang)
                        request.LANGUAGE_CODE = translation.get_language()
                    except AttributeError: pass
