from django.db import models
from .date_time_model import DateTimeModel


# Create your models here.
class NamedDateTimeModel(DateTimeModel):

    name = models.CharField(max_length=180, verbose_name="Nom ")

    class Meta:
        abstract = True

    def __str__(self):
        return self.name