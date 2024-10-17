from rest_framework import serializers
from user.models.custom_user_model import CustomUserModel


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()
