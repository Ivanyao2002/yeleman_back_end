from django.utils.translation import gettext_lazy as _
from django.db import models


# Create your models here.

class CardsTypeEnum(models.TextChoices):

    CNI = "CNI", _("CNI")
    PASSPORT = "PASSPORT", _("PASSPORT")
    ATTESTATION = "ATTESTATION", _("ATTESTATION")
    AUTRE = "AUTRE", _("AUTRE")
