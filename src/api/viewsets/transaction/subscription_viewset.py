from rest_framework import viewsets, mixins
from rest_framework import status
from rest_framework.response import Response
from datetime import timedelta, datetime
from transaction.models.subscription_model import SubscriptionModel
from api.serializers.transaction.subscription_serializer import SubscriptionSerializer


class SubscriptionViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    serializer_class = SubscriptionSerializer
    queryset = SubscriptionModel.objects.filter(status=True)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['ended'] = datetime.today() + timedelta(days=30)
            serializer.save()
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({"detail": "Souscription reussie"}, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
