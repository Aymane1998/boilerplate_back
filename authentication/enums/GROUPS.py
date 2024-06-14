from django.db import models
from django.utils.translation import gettext_lazy as _


class GROUPS(models.TextChoices):
    PARTNER = "PARTNER", _("PARTNER")
    SPF = "SPF", _("SPF")
    UPR = "UPR", _("UPR")
    ADMIN = "ADMIN", _("ADMIN")
