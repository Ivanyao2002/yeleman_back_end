from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins
from property.models.demand_model import DemandModel
from rest_framework import status
from rest_framework.response import Response
from api.serializers.property.location_demand_serializer import LocationDemandSerializer
from api.permissions.is_owner_permission import IsOwnerPermission
from api.permissions.is_tenant_permission import IsTenantPermission
from owner.models.owner_model import OwnerModel
from tenant.models.tenant_model import TenantModel


class LocationDemandViewSet(viewsets.ModelViewSet):
    serializer_class = LocationDemandSerializer

    # def get_permissions(self):
    #     if self.action in ['list', 'patch']:
    #         permission_classes = [IsOwnerPermission]
    #     else:
    #         permission_classes = [IsTenantPermission]
    #     return [permission() for permission in permission_classes]

    def get_queryset(self):
        if self.action in ['list']:
            owner = get_object_or_404(OwnerModel, user=self.request.user)
            return DemandModel.objects.filter(property__owner=owner, status=True, demand_type='LOCATION')
        return DemandModel.objects.filter(status=True, demand_type='LOCATION')

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        last_five_requests_location = DemandModel.objects.filter(
            property__owner__user=request.user, status=True, demand_type='LOCATION'
        ).order_by('-created_at')[:5].count()

        serializer = self.get_serializer(queryset, many=True)

        response_data = {
            'all_requests': serializer.data,
            'last_five_requests': last_five_requests_location
        }

        return Response(response_data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['demand_type'] = 'LOCATION'
            tenant = get_object_or_404(TenantModel, user=request.user)
            serializer.validated_data['tenant'] = tenant
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
