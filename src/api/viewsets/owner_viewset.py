import random
from rest_framework.permissions import AllowAny
from django.utils import timezone
from rest_framework import status, generics
from rest_framework.response import Response
from owner.models.owner_model import OwnerModel
from base.models.otp_token_model import OtpTokenModel
from ..serializers.owner_serialiser import OwnerSerializer
from ..serializers.otp_serializer import OtpSerializer
from django.contrib.auth.hashers import make_password
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from django.core.mail import send_mail
from django.conf import settings


class OwnerViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'put']
    queryset = OwnerModel.objects.filter(is_active=True)
    serializer_class = OwnerSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            serializer.validated_data['user_type'] = 'PROPRIETAIRE'
            owner = serializer.save()
            otp_code = str(random.randint(100000, 999999))
            otp_token = OtpTokenModel.objects.create(user=owner, otp_code=otp_code,
                        otp_expires_at=timezone.now() + timezone.timedelta(minutes=5))
            send_otp(owner.email, otp_code)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({"detail": "Un OTP a été envoyé.",
                             "username": owner.username}, status=status.HTTP_201_CREATED, headers=headers)
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
            return Response({"error": "Le nom d'utilisateur et le code sont requis."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            otp_token = OtpTokenModel.objects.get(user__username=username, otp_code=otp_code)
            if otp_token.otp_expires_at < timezone.now():
                return Response({"detail": "L'OTP a expiré."}, status=status.HTTP_400_BAD_REQUEST)

            owner = otp_token.user
            owner.is_active = True
            owner.save()
            otp_token.delete()
            return Response({"detail": "OTP validé avec succès."}, status=status.HTTP_200_OK)

        except OtpTokenModel.DoesNotExist:
            return Response({"detail": "OTP invalide."}, status=status.HTTP_400_BAD_REQUEST)


def send_otp(email, otp_code):
    subject = 'Votre code OTP'
    message = f'Votre code OTP est : {otp_code}. Il est valide pendant 5 minutes.'
    from_email = settings.DEFAULT_FROM_EMAIL

    try:
        send_mail(subject, message, from_email, [email])
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'OTP : {e}")