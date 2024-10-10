from rest_framework import serializers


class OtpSerializer(serializers.Serializer):
    otp_code = serializers.CharField(max_length=6)
    username = serializers.CharField(max_length=150)