from property.models.demand_model import DemandModel
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from property.models.property_model import PropertyModel


class LocationDemandSerializer(ModelSerializer):
    property = PrimaryKeyRelatedField(queryset=PropertyModel.objects.filter(status=True))

    class Meta:
        model = DemandModel
        fields = ['id', 'tenant', 'property', 'comment']
