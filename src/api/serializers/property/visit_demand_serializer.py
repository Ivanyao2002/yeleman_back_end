from property.models.demand_model import DemandModel
from rest_framework.serializers import ModelSerializer


class VisitDemandSerializer(ModelSerializer):
    class Meta:
        model = DemandModel
        fields = ['id', 'tenant', 'property', 'visit_date', 'comment']
