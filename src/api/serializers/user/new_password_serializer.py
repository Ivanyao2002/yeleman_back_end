from rest_framework import serializers


class NewPasswordSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, write_only=True)
    otp_code = serializers.CharField(max_length=6)