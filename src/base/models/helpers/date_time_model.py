from django.db import models


# Create your models here.
class DateTimeModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création ")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date d'édition ")
    status = models.BooleanField(default=True, verbose_name="Status ")

    class Meta:
        abstract = True