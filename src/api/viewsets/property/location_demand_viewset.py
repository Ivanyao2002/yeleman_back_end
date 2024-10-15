from rest_framework import viewsets, mixins
from property.models.demand_model import DemandModel
from rest_framework import status
from rest_framework.response import Response
from api.serializers.property.location_demand_serializer import LocationDemandSerializer


class LocationDemandViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin,
                            mixins.RetrieveModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = DemandModel.objects.filter(status=True, demand_type='LOCATION')
    serializer_class = LocationDemandSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['demand_type'] = 'LOCATION'
            serializer.save()
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({"detail": "Demande envoyée"}, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
