from django.db import models
from base.models.helpers.date_time_model import DateTimeModel


class SubscriptionModel(DateTimeModel):

    user = models.ForeignKey("base.CustomUserModel", on_delete=models.CASCADE)
    subscription_plan = models.ForeignKey("transaction.SubscriptionPlanModel", on_delete=models.CASCADE)
    ended = models.DateTimeField(verbose_name="Date de fin d'abonnement ")

    def __str__(self):
        return f"Date de debut {self.created_at} - Date de fin {self.ended}"

    class Meta:
        verbose_name = "Abonnement"
        verbose_name_plural = "Abonnements"

