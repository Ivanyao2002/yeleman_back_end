from rest_framework import serializers
from property.models.property_model import PropertyModel


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model= PropertyModel
        fields ="__all__"