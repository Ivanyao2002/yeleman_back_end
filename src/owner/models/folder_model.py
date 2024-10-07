from django.db import models
from base.models.helpers.date_time_model import DateTimeModel


class FolderModel(DateTimeModel):

    owner = models.ForeignKey("owner.OwnerModel", on_delete=models.CASCADE, related_name="folder_owner_id")
    acd_number = models.CharField(max_length=30, verbose_name="Numéro de l'ACD ")
    property_type = models.CharField(max_length=30, verbose_name="Type de propriété ")
    localization = models.CharField(max_length=30, verbose_name="Localisation ")

    def __str__(self):
        return f"{self.acd_number} - {self.property_type}"

    class Meta:
        verbose_name = "Dossier"
        verbose_name_plural = "Dossiers"
