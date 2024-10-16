from django.db import models
from base.models.helpers.date_time_model import DateTimeModel


# Create your models here.

class TenantModel(DateTimeModel):
    user = models.OneToOneField("user.CustomUserModel", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Locataire"
        verbose_name_plural = "Locataires"

    def __str__(self):
        return f"{self.user.username}"
