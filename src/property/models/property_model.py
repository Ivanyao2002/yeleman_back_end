from django.db import models
from base.models.helpers.date_time_model import DateTimeModel


class PropertyModel(DateTimeModel):

    owner = models.ForeignKey("owner.OwnerModel", on_delete=models.CASCADE, related_name="property_owner_id")
    label = models.TextField(verbose_name="Commentaire ")
    price = models.IntegerField(verbose_name="Prix ")
    address = models.IntegerField(verbose_name="Localisation ")
    surface = models.IntegerField(verbose_name="Surface ")
    property_type = models.IntegerField(verbose_name="Type de propriété ")
    description = models.IntegerField(verbose_name="Description ")
    available = models.IntegerField(verbose_name="Disponibilité ")
    bedrooms_number = models.IntegerField(verbose_name="Nombre de chambres ")

    def __str__(self):
        return f"{self.label} - {self.property_type}"

    class Meta:
        verbose_name = "Propriété"
        verbose_name_plural = "Propriétés"
