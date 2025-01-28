from user.models.custom_user_model import CustomUserModel
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = ['id', 'password', 'username', 'first_name', 'last_name', 'email', 'user_type']

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_username(self, value):
        if CustomUserModel.objects.filter(username=value).exists():
            raise serializers.ValidationError("Ce nom d'utilisateur existe déjà !")
        return value

    def validate_email(self, value):
        if CustomUserModel.objects.filter(email=value).exists():
            raise serializers.ValidationError("Ce mail existe déjà !")
        return value