from django.db import models
from base.models.custom_user_model import CustomUserModel


# Create your models here.

class OwnerModel(CustomUserModel):
    folder_status = models.BooleanField(default=False, verbose_name="Etat du dossier ")

    class Meta:
        verbose_name = "Propriétaire"
        verbose_name_plural = "Propriétaires"

