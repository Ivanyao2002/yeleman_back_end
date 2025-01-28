from user.models.custom_user_model import CustomUserModel
from rest_framework import serializers


class PasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True)

    class Meta:
        model = CustomUserModel
        fields = ["old_password", "password"]
        extra_kwargs_fields = {
            "password": {
                'write_only': True
            }
        }