from django.db import models
from base.models.helpers.date_time_model import DateTimeModel


# Create your models here.

class VisitModel(DateTimeModel):

    tenant = models.ForeignKey("tenant.TenantModel", on_delete=models.CASCADE)
    property = models.ManyToManyField("property.PropertyModel", related_name="visit_property_id")
    visit_date = models.DateField(verbose_name="Date de visite ")
    comment = models.TextField(verbose_name="Commentaire ")

    class Meta:
        verbose_name = "Locataire"
        verbose_name_plural = "Locataires"

