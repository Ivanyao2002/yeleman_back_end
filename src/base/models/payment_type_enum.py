from django.utils.translation import gettext_lazy as _
from django.db import models


# Create your models here.

class PaymentTypeEnum(models.TextChoices):

    SUBSCIPTION = "Abonnement", _("Abonnement")
    RENT_PAYMENT = "Paiement de loyer", _("Paiement de loyer")
