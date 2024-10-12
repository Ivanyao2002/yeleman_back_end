from django.db import models
from base.models.helpers.date_time_model import DateTimeModel


# Create your models here.

class DemandModel(DateTimeModel):

    TYPE_CHOICES = [
        ('LOCATION', 'LOCATION'),
        ('VISITE', 'VISITE'),
    ]

    tenant = models.ForeignKey("tenant.TenantModel", on_delete=models.CASCADE)
    property = models.ForeignKey("property.PropertyModel", related_name="visit_property_id", on_delete=models.CASCADE)
    visit_date = models.DateField(verbose_name="Date de visite ", blank=True, null=True)
    comment = models.TextField(verbose_name="Commentaire ", blank=True, null=True)
    demand_type = models.CharField(max_length=15, choices=TYPE_CHOICES, default='VISITE', verbose_name="Type de visite ")
    demand_status = models.BooleanField(default=False, verbose_name="Status de la demande ")

    class Meta:
        verbose_name = "Demande"
        verbose_name_plural = "Demandes"

