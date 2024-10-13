from django.db import models
from base.models.helpers.date_time_model import DateTimeModel


class PropertyModel(DateTimeModel):

    owner = models.ForeignKey("owner.OwnerModel", on_delete=models.CASCADE, related_name="properties")
    label = models.CharField(max_length=50, verbose_name="Libellé ")
    price = models.IntegerField(verbose_name="Prix ")
    address = models.CharField(max_length=50, verbose_name="Localisation ")
    surface = models.FloatField(verbose_name="Surface ")
    property_type = models.CharField(max_length=100, verbose_name="Type de propriété ")
    description = models.TextField(verbose_name="Description ")
    bedrooms_number = models.IntegerField(verbose_name="Nombre de chambres ")
    video_url = models.URLField(verbose_name="Lien de la vidéo ", blank=True, null=True)

    def __str__(self):
        return f"{self.label} - {self.property_type}"

    class Meta:
        verbose_name = "Propriété"
        verbose_name_plural = "Propriétés"
