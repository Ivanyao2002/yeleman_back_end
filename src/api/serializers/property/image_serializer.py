from rest_framework import serializers
from property.models.image_model import ImageModel


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImageModel
        fields = ['id', 'property', 'image']
