.. _installation:

Installation.
=============

Before install django-userena-ce, you'll need to have a copy of `Django
<http://www.djangoproject.com>`_ 2.2 or 3.0 installed. django-userena-ce is
tested under Python 3.6, 3.7 and 3.8 (all versions on which
Django 2.2 and higher is declared to work)

For further information, consult the `Django download page
<http://www.djangoproject.com/download/>`_, which offers convenient packaged
downloads and installation instructions.

Support for old Django and Python Versions
------------------------------------------

From version 5.0.0 only django versions 2.2 and 3.0 will be supported.
Django 1.11 and/or Python 2 users should install ``django-userena-ce<5.0``.

Installing django-userena-ce
----------------------------

You can install django-userena automagically with ``pip``. Or by manually
placing it on on your ``PYTHON_PATH``. The recommended way is the shown in
:ref:`pip-install`.

*It is also recommended to use* `virtualenv
<http://pypi.python.org/pypi/virtualenv>`_ *to have an isolated python
environment. This way it's possible to create a tailored environment for each
project.*

.. _pip-install:

Automatic installation with pip.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Automatic install with `pip
<http://www.pip-installer.org/en/latest/index.html>`_. All you have to do is
run the following command::

    pip install django-userena-ce

If you want to have a specific version of userena, you can do so by adding the
following::

    pip install django-userena-ce==4.0.0

Manual installation with easy_install.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Clone the Git repository from Github. Then you can direct easy_install to the
``setup.py`` file. For ex.::

    git clone git://github.com/django-userena-ce/django-userena-ce.git
    cd django-userena
    easy_install setup.py


Automatic installation of development version with pip.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can tell `pip`_ to install django-userena by supplying it with the git
repository on Github. Do this by typing the following in your terminal::

    pip install -e git+git://github.com/django-userena-ce/django-userena-ce.git#egg=userena


Manual installation of development version with git.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Clone userena with::
    
    git clone git://github.com/django-userena-ce/django-userena-ce.git

You now have a directory ``django-userena`` which contains the ``userena``
application. You can add userena to your ``$PYTHONPATH`` by symlinking it. For
example::

    cd YOUR_PYTHON_PATH
    ln -s ~/src/django-userena/userena userena

Now userena is available to your project.

Start New App
~~~~~~~~~~~~~

You need to create a new app on your Django project. 
In your Command Prompt shell, type: ``python manage.py startapp accounts``. 
We are creating a new app for Userena titled 'accounts'.

Next, add ``accounts`` to the ``INSTALLED_APPS`` in your settings.py file.


Required settings
-----------------

Next, you need to make some changes in the Django settings if you want to use Userena in
your project. This means modifying ``AUTHENTICATION_BACKENDS``,
``INSTALLED_APPS`` and optionally ``MIDDLEWARE_CLASSES``.

Begin by adding ``userena``, ``guardian`` and ``easy_thumbnails`` to the
``INSTALLED_APPS`` in your settings.py file of your project.
``django.contrib.sites`` must also be present if it is not already (see `Django docs
<https://docs.djangoproject.com/en/1.11/ref/contrib/sites/>`_.).

Next add ``UserenaAuthenticationBackend`` and ``ObjectPermissionBackend`` 
also in your settings.py file, from django-guardian, at the top of ``AUTHENTICATION_BACKENDS``. 
If you only have Django's default backend, adding django-guardian and that of userena will get
the following:

.. code-block:: python

    AUTHENTICATION_BACKENDS = (
        'userena.backends.UserenaAuthenticationBackend',
        'guardian.backends.ObjectPermissionBackend',
        'django.contrib.auth.backends.ModelBackend',
    )

Email Backend
~~~~~~~~~~~~~

Userena uses the Django email facilities to send mail to users, for example
after user signup for email verification.  By default Django uses the SMTP
backend, which may cause issues in development and/or if the default SMTP 
settings are not suitable for your environment.  It is recommended to 
explicitly set the email backend provider in your settings.py.  For example:

.. code-block:: python

    EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
    

To use GMail SMTP, you may use the following code in your settings.py:

.. code-block:: python

    EMAIL_USE_TLS = True
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'yourgmailaccount@gmail.com'
    EMAIL_HOST_PASSWORD = 'yourgmailpassword'

See: `Django Email Documentation <https://docs.djangoproject.com/en/dev/topics/email/>`_

Profiles
~~~~~~~~

Userena needs you to define the profile that is used by supplying Django's
``AUTH_PROFILE_MODULE`` setting. Userena supplies the following two base
profiles for you that you should use for your own profile model by inheriting
from them:

    ``UserenaBaseProfile``
        Basic profile that supplies your user with mugshots and the necessary
        fields for privacy settings.

    ``UserenaLanguageBaseProfile``
        Adds an extra field that lets the user define its preferred language
        after logging in to your site.

**IMPORTANT**: The above profiles are ``abstract`` models. This means that you
cannot use them directly in ``AUTH_PROFILE_MODULE`` but you must create your
own profile model which inherits from one of the above models. This models
must also connect itself to the :class:`User` model of Django.

.. code-block:: python

    from django.contrib.auth.models import User
    from django.utils.translation import gettext as _
    from userena.models import UserenaBaseProfile
    
    class MyProfile(UserenaBaseProfile):
        user = models.OneToOneField(User,
                                    unique=True,
                                    verbose_name=_('user'),
                                    related_name='my_profile',
                                    on_delete=models.CASCADE) 
        favourite_snack = models.CharField(_('favourite snack'),
                                           max_length=5)

If you want the user have the ability to choose their default language in their
profile, you must add ``userena.middleware.UserenaLocaleMiddleware`` at the end of
``MIDDLEWARE_CLASSES`` in your Django settings. This does require a profile
model which has a language field. You can use the
``UserenaLanguageBaseProfile`` class of userena that does this for you.

The URI's
~~~~~~~~~

Userena has a ``URLconf`` which sets all the urls and views for you. This
should be included in your project's root ``URLconf``. 

For example, to place the URIs under the prefix ``/accounts/``, you could add
the following to your project's root ``URLconf``. 
Add this code under ``urlpatterns`` in your urls.py file.

.. code-block:: python

    (r'^accounts/', include('userena.urls')),


This should have you a working accounts application for your project. See the
:ref:`settings <settings>` for further configuration options.

Required settings
~~~~~~~~~~~~~~~~~

Django-guardian requires you to set the ``ANONYMOUS_USER_NAME`` setting.
As noted before, you are also required to set the
``AUTH_PROFILE_MODULE`` to your custom defined profile.

For example, add the following into your settings.py file:

.. code-block:: python

    ANONYMOUS_USER_NAME = 'AnonymousUser'

    AUTH_PROFILE_MODULE = 'accounts.MyProfile'

To integrate Django with userena you should alter the following three settings
to reflect the URI you have chosen for userena. For example, if userena lives
under ``accounts``:

.. code-block:: python

    USERENA_SIGNIN_REDIRECT_URL = '/accounts/%(username)s/'
    LOGIN_URL = '/accounts/signin/'
    LOGOUT_URL = '/accounts/signout/'

The above should supply you with a fully functional account management app for
your project. You can look into the next chapter to fully customize userena to
your likings.

To integrate Userena with your domain you must create a Site for it in the
Django admin screen (e.g. http://<yoursite.com>/admin/sites/ ) and then 
put the id for that site in the SITE_ID setting variable.:

.. code-block:: python

   SITE_ID = <site.id of your site> # will probably be '1' if this is your 
                                    # first.
                                    
To look up your site_id open a shell in manage.py (manage.py shell) and:

.. code-block:: python

   from django.contrib.sites.models import Site
   for s in Site.objects.all():
      print "id: {0}  name: {1}".format(s.id, s.name)

Set SITE_ID to the id of the desired name. (eks: 1)

Run Migrations
~~~~~~~~~~~~~~~~
run `python manage.py makemigrations` and `python manage.py migrate`

Permission check
~~~~~~~~~~~~~~~~

Sometimes Django decides to skip installing the default permissions for a
model. To check if all permissions are there, run the ``check_permissions`` in
the management :ref:`commands`.

.. _Github: https://github.com/lukaszb/django-guardian

Migrating from bread-and-pepper/django-userena
==============================================

This project was forked from bread-and-pepper/django-userena v2.0.1. 
To migrate from this project you just need to install the package
and update a key which was changed in django-guardian:

1. Remove `django-userena` from your installation `pip uninstall django-userena`
2. `pip install django-userena-ce==3.1.0`
3. Replace `django-userena` to `django-userena-ce` in your `INSTALLED_APPS`
4. Update your django settings, remove `ANONYMOUS_USER_ID` and set `ANONYMOUS_USER_NAME`

