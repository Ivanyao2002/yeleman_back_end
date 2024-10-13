import random
from rest_framework.permissions import AllowAny
from django.utils import timezone
from rest_framework import status, generics, viewsets, mixins
from rest_framework.response import Response
from tenant.models.tenant_model import TenantModel
from base.models.otp_token_model import OtpTokenModel
from ..serializers.tenant_serialiser import TenantSerializer
from ..serializers.otp_serializer import OtpSerializer
from django.contrib.auth.hashers import make_password
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags


class TenantViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    http_method_names = ['get', 'post', 'put']
    queryset = TenantModel.objects.filter(is_active=True)
    serializer_class = TenantSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            serializer.validated_data['user_type'] = 'LOCATAIRE'
            tenant = serializer.save()
            otp_code = str(random.randint(1000, 9999))
            otp_token = OtpTokenModel.objects.create(user=tenant, otp_code=otp_code,
                                                     otp_expires_at=timezone.now() + timezone.timedelta(minutes=5))
            send_otp(tenant.email, otp_code, tenant)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({"detail": "Un OTP a été envoyé.",
                             "username": tenant.username}, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            serializer.save()
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class OtpVerifyView(generics.GenericAPIView):
    serializer_class = OtpSerializer

    def post(self, request, *args, **kwargs):
        otp_code = request.data.get('otp_code')
        username = request.data.get('username')

        if not username or not otp_code:
            return Response({"error": "Le nom d'utilisateur et le code sont requis."},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            otp_token = OtpTokenModel.objects.get(user__username=username, otp_code=otp_code)
            if otp_token.otp_expires_at < timezone.now():
                return Response({"detail": "L'OTP a expiré."}, status=status.HTTP_400_BAD_REQUEST)

            tenant = otp_token.user
            tenant.is_active = True
            tenant.save()
            otp_token.delete()
            return Response({"detail": "OTP validé avec succès."}, status=status.HTTP_200_OK)

        except OtpTokenModel.DoesNotExist:
            return Response({"detail": "OTP invalide."}, status=status.HTTP_400_BAD_REQUEST)


def send_otp(email_address, otp_code, tenant):
    subject = 'Vérification de votre code OTP'
    html_message = render_to_string('email_otp.html', {'user': tenant, 'otp_code': otp_code})
    plain_message = strip_tags(html_message)
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email_address]

    try:
        email = EmailMultiAlternatives(subject=subject, body=plain_message, from_email=from_email, to=recipient_list)
        email.attach_alternative(html_message, "text/html")
        email.send()
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'OTP : {e}")
