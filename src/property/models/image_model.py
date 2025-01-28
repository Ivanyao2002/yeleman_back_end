from base.models.helpers.date_time_model import DateTimeModel
from django.db import models
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile


FILE_UPLOAD_MAX_MEMORY_SIZE = 1024 * 1024 * 10  # 10mb


def file_validation(file):
    if not file:
        raise ValidationError("Aucun fichier selectionné")

    if isinstance(file, UploadedFile):
        if file.size > FILE_UPLOAD_MAX_MEMORY_SIZE:
            raise ValidationError("Le fichier ne doit pas exceder 10MB.")


class ImageModel(DateTimeModel):
    property = models.ForeignKey("property.PropertyModel", on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('image', folder='Properties', validators=[file_validation], blank=True, null=True)

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"