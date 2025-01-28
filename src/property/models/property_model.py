import secrets

from django.db import models
from base.models.helpers.date_time_model import DateTimeModel
from django.template.defaultfilters import slugify


class PropertyModel(DateTimeModel):

    TYPE_CHOICES = [
        ('Appartement', 'Appartement'),
        ('Villa', 'Villa'),
        ('Studio', 'Studio'),
        ('Duplex', 'Duplex'),
    ]
    STATE_CHOICES = [
        ('Maintenance', 'Maintenance'),
        ('Disponible', 'Disponible'),
        ('Occupée', 'Occupée'),
    ]

    owner = models.ForeignKey("owner.OwnerModel", on_delete=models.CASCADE, related_name="properties")
    label = models.CharField(max_length=50, verbose_name="Libellé ")
    price = models.IntegerField(verbose_name="Prix ")
    address = models.CharField(max_length=50, verbose_name="Localisation ")
    city = models.CharField(max_length=50, verbose_name="Ville ")
    surface = models.FloatField(verbose_name="Surface ")
    property_type = models.CharField(max_length=30, choices=TYPE_CHOICES, default='Villa',
                                     verbose_name="Type de propriété ")
    description = models.TextField(verbose_name="Description ")
    bedrooms_number = models.IntegerField(verbose_name="Nombre de chambres ")
    bathrooms_number = models.IntegerField(verbose_name="Nombre de salles de bains ")
    video_url = models.URLField(verbose_name="Lien de la vidéo ", blank=True, null=True)
    state = models.CharField(max_length=13, choices=STATE_CHOICES, default='Disponible', verbose_name='Status ')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.label} - {self.property_type}"

    class Meta:
        verbose_name = "Propriété"
        verbose_name_plural = "Propriétés"

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(f"{self.label}-{secrets.token_urlsafe(3)}")

        super(PropertyModel, self).save(*args, **kwargs)
