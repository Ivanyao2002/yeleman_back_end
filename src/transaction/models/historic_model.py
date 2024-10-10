from django.db import models
from base.models.helpers.date_time_model import DateTimeModel


class HistoricModel(DateTimeModel):

    owner = models.ForeignKey("owner.OwnerModel", on_delete=models.CASCADE, blank=True, null=True)
    tenant = models.ForeignKey("tenant.TenantModel", on_delete=models.CASCADE, blank=True, null=True)
    subscription_plan = models.ForeignKey("transaction.SubscriptionPlanModel", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subscription_plan}"

    class Meta:
        verbose_name = "Historique"
        verbose_name_plural = "Historiques"
