from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from guardian.admin import GuardedModelAdmin

from userena import settings as userena_settings
from userena.models import UserenaSignup
from userena.utils import get_profile_model


class UserenaSignupInline(admin.StackedInline):
    model = UserenaSignup
    max_num = 1


class UserenaAdmin(UserAdmin, GuardedModelAdmin):
    inlines = [UserenaSignupInline]
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
        "date_joined",
    )
    list_filter = ("is_staff", "is_superuser", "is_active")


if userena_settings.USERENA_REGISTER_USER:
    try:
        admin.site.unregister(get_user_model())
    except admin.sites.NotRegistered:
        pass

    admin.site.register(get_user_model(), UserenaAdmin)

if userena_settings.USERENA_REGISTER_PROFILE:
    admin.site.register(get_profile_model(), GuardedModelAdmin)
