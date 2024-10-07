from django.db import models
from base.models.helpers.date_time_model import DateTimeModel


class CharacteristicPropertyModel(DateTimeModel):

    property = models.OneToOneField("property.PropertyModel", on_delete=models.CASCADE, related_name="characteristic_property_id")
    swimming_pool = models.BooleanField(verbose_name="Commentaire ")
    green_space = models.BooleanField(verbose_name="Espace vert ")
    air_conditioning = models.BooleanField(verbose_name="Climatisation ")
    nearby_school_or_university = models.BooleanField(verbose_name="A proximité Ecole/Université ")
    commercial_area = models.BooleanField(verbose_name="En zone commerciale ")
    garden = models.BooleanField(verbose_name="Jardin ")
    quiet_area = models.BooleanField(verbose_name="Quartier calme ")
    balcony_terrace = models.BooleanField(verbose_name="Balcon / Terrasse ")
    gym_room = models.BooleanField(verbose_name="Salle de sport ")
    furnished = models.BooleanField(verbose_name="Meublé ")
    furnished_kitchen = models.BooleanField(verbose_name="Cuisine Meublée ")
    city_center = models.BooleanField(verbose_name="En centre-ville ")
    general_condition_new = models.BooleanField(verbose_name="Etat général: Neuf ")
    guardian = models.BooleanField(verbose_name="Gardien ")

    def __str__(self):
        return f"{self.general_condition_new}"

    class Meta:
        verbose_name = "Caractéristique"
        verbose_name_plural = "Caractéristiques"
