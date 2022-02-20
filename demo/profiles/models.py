import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _

from userena.models import UserenaLanguageBaseProfile
from userena.utils import user_model_label


class Profile(UserenaLanguageBaseProfile):
    """Default profile"""

    user = models.OneToOneField(
        user_model_label,
        unique=True,
        verbose_name=_("user"),
        related_name="profile",
        on_delete=models.CASCADE,
    )

    website = models.URLField(_("website"), blank=True)
    location = models.CharField(_("location"), max_length=255, blank=True)
    birth_date = models.DateField(_("birth date"), blank=True, null=True)
    about_me = models.TextField(_("about me"), blank=True)

    @property
    def age(self):
        if not self.birth_date:
            return False
        else:
            today = datetime.date.today()
            # Raised when birth date is February 29 and the current year is not a
            # leap year.
            try:
                birthday = self.birth_date.replace(year=today.year)
            except ValueError:
                day = today.day - 1 if today.day != 1 else today.day + 2
                birthday = self.birth_date.replace(year=today.year, day=day)
            if birthday > today:
                return today.year - self.birth_date.year - 1
            else:
                return today.year - self.birth_date.year
