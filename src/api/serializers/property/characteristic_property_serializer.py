from rest_framework import serializers
from property.models.characteristic_property_model import CharacteristicPropertyModel


class CharacteristicPropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = CharacteristicPropertyModel
        fields = ['id', 'swimming_pool', 'green_space', 'air_conditioning', 'nearby_school_or_university',
                  'commercial_area', 'garden', 'quiet_area', 'balcony_terrace', 'gym_room', 'furnished',
                  'furnished_kitchen', 'city_center', 'general_condition_new', 'guardian']
