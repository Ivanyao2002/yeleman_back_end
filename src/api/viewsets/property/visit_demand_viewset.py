from rest_framework.viewsets import ModelViewSet
from property.models.demand_model import DemandModel
from api.serializers.property.visit_demand_serializer import VisitDemandSerializer


class VisitDemandViewSet(ModelViewSet):
    queryset = DemandModel.objects.filter(status=True, demand_type='VISITE')
    serializer_class = VisitDemandSerializer
