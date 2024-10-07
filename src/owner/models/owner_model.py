from django.db import models
from base.models.custom_user_model import CustomUserModel


# Create your models here.

class OwnerModel(CustomUserModel):
    pass

    class Meta:
        verbose_name = "Propriétaire"
        verbose_name_plural = "Propriétaires"

