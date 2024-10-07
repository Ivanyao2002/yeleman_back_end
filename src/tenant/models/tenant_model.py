from django.db import models
from base.models.custom_user_model import CustomUserModel


# Create your models here.

class TenantModel(CustomUserModel):
    pass

    class Meta:
        verbose_name = "Locataire"
        verbose_name_plural = "Locataires"
