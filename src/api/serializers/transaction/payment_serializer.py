from rest_framework import serializers
from transaction.models.payment_model import PaymentModel


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentModel
        fields = ['id', 'user', 'payment_type']
