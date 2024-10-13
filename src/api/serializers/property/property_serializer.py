from rest_framework import serializers
from property.models.property_model import PropertyModel
from owner.models.owner_model import OwnerModel
from .characteristic_property_serializer import CharacteristicPropertySerializer
from property.models.characteristic_property_model import CharacteristicPropertyModel


class PropertySerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=OwnerModel.objects.filter(is_active=True))
    characteristics = CharacteristicPropertySerializer(many=True)

    class Meta:
        model = PropertyModel
        fields = ['id', 'owner', 'label', 'price', 'address', 'surface', 'property_type', 'description',
                  'bedrooms_number', 'characteristics']

    def create(self, validated_data):
        characteristics_data = validated_data.pop('characteristics')
        property_instance = PropertyModel.objects.create(**validated_data)
        for char_data in characteristics_data:
            CharacteristicPropertyModel.objects.create(property=property_instance, **char_data)
        return property_instance

    def update(self, instance, validated_data):
        characteristics_data = validated_data.pop('characteristics', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if characteristics_data is not None:
            instance.characteristics.all().delete()
            for char_data in characteristics_data:
                CharacteristicPropertyModel.objects.create(property=instance, **char_data)

        return instance
