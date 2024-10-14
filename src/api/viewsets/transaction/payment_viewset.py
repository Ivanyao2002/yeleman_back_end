from rest_framework import viewsets, mixins
from transaction.models.payment_model import PaymentModel
from api.serializers.transaction.payment_serializer import PaymentSerializer


class PaymentViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):
    serializer_class = PaymentSerializer
    queryset = PaymentModel.objects.filter(status=True)
