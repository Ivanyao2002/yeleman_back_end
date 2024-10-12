from rest_framework import viewsets, mixins
from property.models.demand_model import DemandModel
from rest_framework import status
from rest_framework.response import Response
from api.serializers.property.visit_demand_serializer import VisitDemandSerializer


class VisitDemandViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = DemandModel.objects.all()
    serializer_class = VisitDemandSerializer
