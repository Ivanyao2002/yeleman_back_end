from django.db import models
from base.models.helpers.date_time_model import DateTimeModel


# Create your models here.

class DemandModel(DateTimeModel):
    TYPE_CHOICES = [
        ('LOCATION', 'LOCATION'),
        ('VISITE', 'VISITE'),
    ]
    STATUT_CHOICES = [
        ('EN_ATTENTE', 'EN_ATTENTE'),
        ('ACCEPTER', 'ACCEPTER'),
        ('REFUSER', 'REFUSER'),
    ]

    tenant = models.ForeignKey("tenant.TenantModel", on_delete=models.CASCADE)
    property = models.ForeignKey("property.PropertyModel", related_name="visits", on_delete=models.CASCADE)
    visit_date = models.DateField(verbose_name="Date de visite ", blank=True, null=True)
    comment = models.TextField(verbose_name="Commentaire ", blank=True, null=True)
    demand_type = models.CharField(max_length=15, choices=TYPE_CHOICES, default='VISITE',
                                   verbose_name="Type de demande ")
    demand_status = models.CharField(max_length=15, choices=STATUT_CHOICES, default="EN_ATTENTE",
                                     verbose_name="Status de la demande ")

    class Meta:
        verbose_name = "Demande"
        verbose_name_plural = "Demandes"
        indexes = [
            models.Index(fields=['demand_status']),
            models.Index(fields=['demand_type']),
        ]

    def __str__(self):
        return f"{self.demand_type} - {self.property} - {self.visit_date}"

    def accepter(self):
        self.demand_status = 'ACCEPTER'
        self.save()

    def refuser(self):
        self.demand_status = 'REFUSER'
        self.save()
