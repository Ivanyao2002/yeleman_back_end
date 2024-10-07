from django.utils.translation import gettext_lazy as _
from django.db import models


# Create your models here.

class AccountTypeEnum(models.TextChoices):

    FREEMIUM = "Standard", _("Standard")
    PREMIUM = "Premium", _("Premium")
