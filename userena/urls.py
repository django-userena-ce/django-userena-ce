from django.contrib.auth import views as auth_views
from django.urls import re_path, reverse_lazy

from userena import settings as userena_settings
from userena import views as userena_views

urlpatterns = [
    # Signup, signin and signout
    re_path(r"^signup/$", userena_views.signup, name="userena_signup"),
    re_path(r"^signin/$", userena_views.signin, name="userena_signin"),
    re_path(r"^signout/$", userena_views.SignoutView.as_view(), name="userena_signout"),
    # Reset password
    re_path(
        r"^password/reset/$",
        auth_views.PasswordResetView.as_view(
            template_name="userena/password_reset_form.html",
            email_template_name="userena/emails/password_reset_message.txt",
            extra_context={
                "without_usernames": userena_settings.USERENA_WITHOUT_USERNAMES
            },
            success_url=reverse_lazy("userena_password_reset_done"),
        ),
        name="userena_password_reset",
    ),
    re_path(
        r"^password/reset/done/$",
        auth_views.PasswordResetDoneView.as_view(
            template_name="userena/password_reset_done.html"
        ),
        name="userena_password_reset_done",
    ),
    re_path(
        r"^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="userena/password_reset_confirm_form.html",
            success_url=reverse_lazy("userena_password_reset_complete"),
        ),
        name="userena_password_reset_confirm",
    ),
    re_path(
        r"^password/reset/confirm/complete/$",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="userena/password_reset_complete.html"
        ),
        name="userena_password_reset_complete",
    ),
    # Signup
    re_path(
        r"^(?P<username>[\@\.\+\w-]+)/signup/complete/$",
        userena_views.direct_to_user_template,
        {
            "template_name": "userena/signup_complete.html",
            "extra_context": {
                "userena_activation_required": userena_settings.USERENA_ACTIVATION_REQUIRED,
                "userena_activation_days": userena_settings.USERENA_ACTIVATION_DAYS,
            },
        },
        name="userena_signup_complete",
    ),
    # Activate
    re_path(
        r"^activate/(?P<activation_key>\w+)/$",
        userena_views.activate,
        name="userena_activate",
    ),
    # Retry activation
    re_path(
        r"^activate/retry/(?P<activation_key>\w+)/$",
        userena_views.activate_retry,
        name="userena_activate_retry",
    ),
    # Activate pending
    re_path(
        r"^(?P<username>[\@\.\+\w-]+)/pending/$",
        userena_views.activate_pending,
        name="userena_activate_pending",
    ),
    # Change email and confirm it
    re_path(
        r"^(?P<username>[\@\.\+\w-]+)/email/$",
        userena_views.email_change,
        name="userena_email_change",
    ),
    re_path(
        r"^(?P<username>[\@\.\+\w-]+)/email/complete/$",
        userena_views.direct_to_user_template,
        {"template_name": "userena/email_change_complete.html"},
        name="userena_email_change_complete",
    ),
    re_path(
        r"^(?P<username>[\@\.\+\w-]+)/confirm-email/complete/$",
        userena_views.direct_to_user_template,
        {"template_name": "userena/email_confirm_complete.html"},
        name="userena_email_confirm_complete",
    ),
    re_path(
        r"^confirm-email/(?P<confirmation_key>\w+)/$",
        userena_views.email_confirm,
        name="userena_email_confirm",
    ),
    # Disabled account
    re_path(
        r"^(?P<username>[\@\.\+\w-]+)/disabled/$",
        userena_views.disabled_account,
        name="userena_disabled",
    ),
    # Change password
    re_path(
        r"^(?P<username>[\@\.\+\w-]+)/password/$",
        userena_views.password_change,
        name="userena_password_change",
    ),
    re_path(
        r"^(?P<username>[\@\.\+\w-]+)/password/complete/$",
        userena_views.direct_to_user_template,
        {"template_name": "userena/password_complete.html"},
        name="userena_password_change_complete",
    ),
    # Edit profile
    re_path(
        r"^(?P<username>[\@\.\+\w-]+)/edit/$",
        userena_views.profile_edit,
        name="userena_profile_edit",
    ),
    # View profiles
    re_path(
        r"^(?P<username>(?!(signout|signup|signin)/)[\@\.\+\w-]+)/$",
        userena_views.profile_detail,
        name="userena_profile_detail",
    ),
    re_path(
        r"^page/(?P<page>[0-9]+)/$",
        userena_views.ProfileListView.as_view(),
        name="userena_profile_list_paginated",
    ),
    re_path(
        r"^$", userena_views.ProfileListView.as_view(), name="userena_profile_list"
    ),
]
