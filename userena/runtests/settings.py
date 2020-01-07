# Django settings for Userena demo project.
DEBUG = True

import os

settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(settings_dir)

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(PROJECT_ROOT, "private/development.db"),
    }
}

# Internationalization
TIME_ZONE = "America/Chicago"
LANGUAGE_CODE = "en-us"
gettext = lambda s: s
LANGUAGES = (
    ("en", gettext("English")),
    ("nl", gettext("Dutch")),
    ("fr", gettext("French")),
    ("pl", gettext("Polish")),
    ("pt", gettext("Portugese")),
    ("pt-br", gettext("Brazilian Portuguese")),
    ("es", gettext("Spanish")),
    ("el", gettext("Greek")),
    ("zh-hans", gettext("Simplified Chinese")),
    ("zh-hant", gettext("Traditional Chinese")),
)
LOCALE_PATHS = (os.path.join(PROJECT_ROOT, "locale"),)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "public/media/")
MEDIA_URL = "/media/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, "public/static/")
STATIC_URL = "/static/"

STATICFILES_DIRS = (os.path.join(PROJECT_ROOT, "demo/static/"),)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = "_g-js)o8z#8=9pr1&amp;05h^1_#)91sbo-)g^(*=-+epxmt4kc9m#"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            # insert your TEMPLATE_DIRS here
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

MIDDLEWARE = (
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "userena.middleware.UserenaLocaleMiddleware",
)

# Add the Guardian and userena authentication backends
AUTHENTICATION_BACKENDS = (
    "userena.backends.UserenaAuthenticationBackend",
    "guardian.backends.ObjectPermissionBackend",
    "django.contrib.auth.backends.ModelBackend",
)

# Settings used by Userena
LOGIN_REDIRECT_URL = "/accounts/%(username)s/"
LOGIN_URL = "/accounts/signin/"
LOGOUT_URL = "/accounts/signout/"
AUTH_PROFILE_MODULE = "profiles.Profile"
USERENA_DISABLE_PROFILE_LIST = True
USERENA_MUGSHOT_SIZE = 140

ROOT_URLCONF = "userena.runtests.urls"
WSGI_APPLICATION = "demo.wsgi.application"

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
    "django.contrib.admindocs",
    "guardian",
    "userena",
    "userena.contrib.umessages",
    "userena.tests.profiles",
)

INSTALLED_APPS += ("easy_thumbnails",)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        }
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        }
    },
}

ANONYMOUS_USER_NAME = "AnonymousUser"

USERENA_USE_HTTPS = False
