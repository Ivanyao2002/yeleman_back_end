from django.db import models
from base.models.helpers.date_time_model import DateTimeModel


# Create your models here.

class OwnerModel(DateTimeModel):
    user = models.OneToOneField("user.CustomUserModel", on_delete=models.CASCADE)
    folder_status = models.BooleanField(default=False, verbose_name="Etat du dossier ")

    class Meta:
        verbose_name = "Propriétaire"
        verbose_name_plural = "Propriétaires"

    def __str__(self):
        return f"{self.user.username}"

