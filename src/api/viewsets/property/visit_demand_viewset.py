from rest_framework import viewsets, mixins
from property.models.demand_model import DemandModel
from api.serializers.property.visit_demand_serializer import VisitDemandSerializer


class VisitDemandViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin,
                            mixins.RetrieveModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = DemandModel.objects.filter(status=True, demand_type='VISITE')
    serializer_class = VisitDemandSerializer
