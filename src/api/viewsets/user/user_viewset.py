import logging
import random
from rest_framework.permissions import AllowAny
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status, mixins, viewsets
from user.models.custom_user_model import CustomUserModel
from user.models.otp_token_model import OtpTokenModel
from api.serializers.user.user_serialiser import UserSerializer
from api.serializers.otp_serializer import OtpSerializer
from django.contrib.auth.hashers import make_password
from owner.models.owner_model import OwnerModel
from tenant.models.tenant_model import TenantModel
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from rest_framework_simplejwt.tokens import RefreshToken

logger = logging.getLogger(__name__)


class UserViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    queryset = CustomUserModel.objects.filter(is_active=True)
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            user = serializer.save()
            if serializer.validated_data['user_type'] == 'PROPRIETAIRE':
                owner = OwnerModel.objects.create(user=user)
            else:
                tenant = TenantModel.objects.create(user=user)
            otp_code = str(random.randint(1000, 9999))
            otp_token = OtpTokenModel.objects.create(user=user, otp_code=otp_code,
                                                     otp_expires_at=timezone.now() + timezone.timedelta(minutes=5))
            send_otp(user.email, otp_code, user.username)

            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({
                "detail": "Un OTP a été envoyé.",
                "username": user.username,
            }, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            if 'password' in serializer.validated_data:
                serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
                serializer.save()
                self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
                return Response({"detail": "L'OTP a expiré."}, status=status.HTTP_400_BAD_REQUEST)

            user = otp_token.user
            user.is_active = True
            user.save()
            otp_token.delete()
            refresh = RefreshToken.for_user(user)
            return Response({
                "detail": "OTP validé avec succès.",
                "refresh": str(refresh),
                "access": str(refresh.access_token),
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
            otp_code = str(random.randint(1000, 9999))
            otp_token = OtpTokenModel.objects.create(user=user, otp_code=otp_code,
                                                     otp_expires_at=timezone.now() + timezone.timedelta(minutes=5))

            send_otp(user.email, otp_code, user.username)

            return Response({"detail": "Un nouveau code OTP a été envoyé."}, status=status.HTTP_200_OK)

        except CustomUserModel.DoesNotExist:
            return Response({"detail": "Utilisateur non trouvé."}, status=status.HTTP_404_NOT_FOUND)


def send_otp(email_address, otp_code, user):
    subject = 'Vérification de votre code OTP'
    html_message = render_to_string('email_otp.html', {'user': user, 'otp_code': otp_code})
    plain_message = strip_tags(html_message)
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email_address]

    try:
        email = EmailMultiAlternatives(subject=subject, body=plain_message, from_email=from_email, to=recipient_list)
        email.attach_alternative(html_message, "text/html")
        email.send()
    except Exception as e:
        logger.error(f"Erreur lors de l'envoi de l'OTP : {e}")
