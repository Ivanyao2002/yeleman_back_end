from base.models.custom_user_model import CustomUserModel
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):

    class Meta:
        model = CustomUserModel
        fields = ['id', 'password', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'cards_type',
                  'num_cni', 'user_type']
