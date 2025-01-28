import logging
import random
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.response import Response
from rest_framework import status, mixins, viewsets
from rest_framework.decorators import action
from api.serializers.user.user_serialiser import UserSerializer
from api.serializers.user.profile_serializer import ProfileSerializer
from api.serializers.user.password_serializer import PasswordSerializer
from user.models.custom_user_model import CustomUserModel
from user.models.otp_token_model import OtpTokenModel
from owner.models.owner_model import OwnerModel
from tenant.models.tenant_model import TenantModel

logger = logging.getLogger(__name__)


class UserViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = CustomUserModel.objects.filter(is_active=True)
    serializer_class = UserSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        print(serializer)
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

            headers = self.get_success_headers(serializer.data)
            return Response({
                "detail": "Un OTP a été envoyé.",
                "username": user.username,
            }, status=status.HTTP_201_CREATED, headers=headers)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['patch'], url_path='update-profile', serializer_class=ProfileSerializer,
            permission_classes=[IsAuthenticated])
    def edit_profile(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = request.user
        serializer = self.get_serializer(request.user, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    @action(detail=False, methods=['put'], url_path='change-password', serializer_class=PasswordSerializer,
            permission_classes=[IsAuthenticated])
    def change_password(self, request, pk=None):
        user = request.user
        old_password = request.data.get('old_password')

        serializer = PasswordSerializer(user, data=request.data)
        if serializer.is_valid():
            if not user.check_password(old_password):
                return Response({"error": "L'ancien mot de passe entré est incorrect !"}, status=400)
            user.password = make_password(serializer.validated_data['password'])
            user.save()
            return Response({'detail': 'Mot de passe changé avec succès !'}, status=201)
        return Response(serializer.errors, status=400)


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