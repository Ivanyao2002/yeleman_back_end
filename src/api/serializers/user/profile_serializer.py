from user.models.custom_user_model import CustomUserModel
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = ['username', 'first_name', 'last_name','avatar', 'phone_number',
                  'num_cni', 'image_recto', 'image_verso', 'cards_type']
