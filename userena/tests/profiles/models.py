from django.db import models
from django.utils.translation import gettext_lazy as _

from userena.models import UserenaBaseProfile
from userena.utils import user_model_label


class Profile(UserenaBaseProfile):
    """ Default profile """

    GENDER_CHOICES = ((1, _("Male")), (2, _("Female")))

    user = models.OneToOneField(
        user_model_label,
        unique=True,
        verbose_name=_("user"),
        related_name="profile",
        on_delete=models.CASCADE,
    )

    gender = models.PositiveSmallIntegerField(
        _("gender"), choices=GENDER_CHOICES, blank=True, null=True
    )
    website = models.URLField(_("website"), blank=True)
    location = models.CharField(_("location"), max_length=255, blank=True)
    about_me = models.TextField(_("about me"), blank=True)
    language = models.TextField(_("language"), blank=True)

    class Meta(UserenaBaseProfile.Meta):
        ordering = ["user"]


class SecondProfile(UserenaBaseProfile):
    user = models.OneToOneField(
        user_model_label,
        unique=True,
        verbose_name=_("user"),
        related_name="profile_second",
        on_delete=models.CASCADE,
    )
