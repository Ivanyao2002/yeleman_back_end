import random
from django.utils import timezone
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status, viewsets
from .user_viewset import send_otp
from api.serializers.user.otp_serializer import OtpSerializer
from user.models.custom_user_model import CustomUserModel
from user.models.otp_token_model import OtpTokenModel
from api.serializers.user.custom_token_obtain_pair_serializer import CustomTokenObtainPairSerializer


class OtpVerifyViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]
    serializer_class = OtpSerializer

    def create(self, request):
        otp_code = request.data.get('otp_code')
        username = request.data.get('username')

        if not username or not otp_code:
            return Response({"error": "Le nom d'utilisateur et le code sont requis."},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            otp_token = OtpTokenModel.objects.get(user__username=username, otp_code=otp_code)
            if otp_token.otp_expires_at < timezone.now():
                otp_token.delete()
                return Response({"detail": "L'OTP a expiré."}, status=status.HTTP_400_BAD_REQUEST)

            user = otp_token.user
            user.is_active = True
            user.save()
            otp_token.delete()

            token = CustomTokenObtainPairSerializer.get_token(user)
            return Response({
                "detail": "OTP validé avec succès.",
                "access": str(token.access_token),
                "refresh": str(token),
            }, status=status.HTTP_200_OK)

        except OtpTokenModel.DoesNotExist:
            return Response({"detail": "OTP invalide."}, status=status.HTTP_400_BAD_REQUEST)

    def regenerate_otp(self, request):
        username = request.data.get('username')

        if not username:
            return Response({"error": "Le nom d'utilisateur est requis."},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            user = CustomUserModel.objects.get(username=username)
            OtpTokenModel.objects.filter(user=user).delete()
            otp_code = str(random.randint(1000, 9999))
            otp_token = OtpTokenModel.objects.create(user=user, otp_code=otp_code,
                                                     otp_expires_at=timezone.now() + timezone.timedelta(minutes=5))

            send_otp(user.email, otp_code, user.username)

            return Response({"detail": "Un nouveau code OTP a été envoyé."}, status=status.HTTP_200_OK)

        except CustomUserModel.DoesNotExist:
            return Response({"detail": "Utilisateur non trouvé."}, status=status.HTTP_404_NOT_FOUND)