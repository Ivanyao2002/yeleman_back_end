import logging
import random
from django.utils import timezone
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from .user_viewset import send_otp
from user.models.custom_user_model import CustomUserModel
from user.models.otp_token_model import OtpTokenModel
from api.serializers.user.new_password_serializer import NewPasswordSerializer
from api.serializers.user.otp_serializer import OtpSerializer
from api.serializers.user.email_serializer import EmailSerializer

logger = logging.getLogger(__name__)


class ResetPasswordViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def create(self, request):
        """
        Étape 1 : Vérification de l'existence du mail et envoi de l'OTP.
        """
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                user = CustomUserModel.objects.get(email=email)
                otp_code = str(random.randint(1000, 9999))  # Générer un code OTP
                OtpTokenModel.objects.update_or_create(
                    user=user,
                    defaults={
                        'otp_code': otp_code,
                        'otp_expires_at': timezone.now() + timezone.timedelta(minutes=5)  # L'OTP expire dans 5 minutes
                    }
                )
                send_otp(user.email, otp_code, user.username)  # Envoyer l'OTP par e-mail

                return Response(
                    {
                        "detail": "Un OTP a été envoyé par mail.",
                        "username": user.username,
                    }, status=status.HTTP_200_OK
                )
            except CustomUserModel.DoesNotExist:
                return Response(
                    {"error": "Le mail que vous avez fournis n'existe pas."},
                    status=status.HTTP_404_NOT_FOUND
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='verify-otp')
    def verify_otp(self, request):
        """
        Étape 2 : Vérification de l'OTP.
        """
        serializer = OtpSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            otp_code = serializer.validated_data['otp_code']

            try:
                user = CustomUserModel.objects.get(username=username)
                otp_token = OtpTokenModel.objects.get(user=user, otp_code=otp_code)

                # Vérifiez si l'OTP a expiré
                if timezone.now() > otp_token.otp_expires_at:
                    otp_token.delete()
                    return Response({"error": "L'OTP a expiré."}, status=status.HTTP_400_BAD_REQUEST)

                return Response({"detail": "OTP vérifié avec succès.", 'otp_code': otp_token.otp_code},
                                status=status.HTTP_200_OK)

            except CustomUserModel.DoesNotExist:
                return Response({"error": "Utilisateur avec cet nom d'utilisateur n'existe pas."},
                                status=status.HTTP_404_NOT_FOUND)
            except OtpTokenModel.DoesNotExist:
                return Response({"error": "OTP invalide."}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='new-password')
    def new_password(self, request):
        """
        Étape 3 : Changement de mot de passe.
        """

        serializer = NewPasswordSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            otp_code = serializer.validated_data['otp_code']
            new_password = serializer.validated_data['new_password']

            try:
                user = CustomUserModel.objects.get(username=username)
                otp_token = OtpTokenModel.objects.get(user=user, otp_code=otp_code)

                # Changez le mot de passe
                user.set_password(new_password)
                user.save()

                # Supprimez l'OTP après utilisation
                otp_token.delete()

                return Response({"detail": "Le mot de passe a été rénitialisé avec succès."}, status=status.HTTP_200_OK)

            except CustomUserModel.DoesNotExist:
                return Response({"error": "Utilisateur avec ce nom d'utilisateur n'existe pas."},
                                status=status.HTTP_404_NOT_FOUND)
            except OtpTokenModel.DoesNotExist:
                return Response({"error": "OTP invalide."}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)