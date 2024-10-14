from rest_framework import serializers
from transaction.models.subscription_model import SubscriptionModel


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubscriptionModel
        fields = ['id', 'user', 'subscription_plan']
