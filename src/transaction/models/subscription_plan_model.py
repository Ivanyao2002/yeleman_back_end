from django.db import models
from base.models.helpers.named_date_time_model import NamedDateTimeModel


# Create your models here.

class SubscriptionPlanModel(NamedDateTimeModel):

    description = models.TextField(verbose_name="Description ")
    price = models.IntegerField(verbose_name="Prix ")

    class Meta:
        verbose_name = "Plan d'abonnement"
        verbose_name_plural = "Plan d'abonnements"

