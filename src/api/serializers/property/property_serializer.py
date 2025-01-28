from rest_framework import serializers
from property.models.property_model import PropertyModel
from .characteristic_property_serializer import CharacteristicPropertySerializer
from .image_serializer import ImageSerializer
from property.models.characteristic_property_model import CharacteristicPropertyModel
from property.models.image_model import ImageModel


class PropertySerializer(serializers.ModelSerializer):
    characteristics = CharacteristicPropertySerializer(many=True)
    images = ImageSerializer(many=True, read_only=True)
    extra_kwargs = {
        'status': {'label': 'Publuée'}
    }

    class Meta:
        model = PropertyModel
        fields = ['id', 'label', 'price', 'address', 'surface', 'property_type', 'description', 'slug',
                  'bedrooms_number', 'bathrooms_number', 'characteristics', 'images', 'status', 'state', 'city']
        extra_kwargs = {
            # 'status': {
            #   'read_only': True
            # },
            'state': {
                'read_only': True
            },
            'slug': {
                'read_only': True
            },
        }

    def create(self, validated_data):
        characteristics_data = validated_data.pop('characteristics')

        property_instance = PropertyModel.objects.create(**validated_data)
        for char_data in characteristics_data:
            CharacteristicPropertyModel.objects.create(property=property_instance, **char_data)

        return property_instance

    def update(self, instance, validated_data):
        characteristics_data = validated_data.pop('characteristics', None)
        images_data = validated_data.pop('images', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if characteristics_data is not None:
            instance.characteristics.all().delete()
            for char_data in characteristics_data:
                CharacteristicPropertyModel.objects.create(property=instance, **char_data)
        if images_data is not None:
            for img_data in images_data:
                ImageModel.objects.create(property=instance, **img_data)

        return instance
