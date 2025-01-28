from rest_framework import viewsets, status
from rest_framework.response import Response
from property.models.property_model import PropertyModel
from property.models.demand_model import DemandModel
from owner.models.owner_model import OwnerModel
from tenant.models.tenant_model import TenantModel


class OwnerDashboardView(viewsets.ViewSet):
    def list(self, request):
        owner = OwnerModel.objects.get(user=request.user)

        properties = PropertyModel.objects.filter(owner=owner)
        property_count = properties.count()

        # tenants = TenantModel.objects.filter(property__in=properties)
        tenants = DemandModel.objects.filter(demand_type='LOCATION', property__owner__user=request.user,
                                             demand_status='ACCEPTER')
        # tenants = TenantModel.objects.all()
        tenant_count = tenants.count()

        visit_demands = DemandModel.objects.filter(demand_type='VISITE', property__owner__user=request.user)
        visit_demand_count = visit_demands.count()

        location_demands = DemandModel.objects.filter(demand_type='LOCATION', property__owner__user=request.user)
        location_demand_count = location_demands.count()


        rented_count = properties.filter(state='Occupée').count()
        not_rented_count = properties.exclude(state='Occupée').count()

        dashboard_data = {
            'total_properties': property_count,
            'total_visit_requests': visit_demand_count,
            'total_location_requests': location_demand_count,
            'total_rented': rented_count,
            'total_not_rented': not_rented_count,
            'total_tenant': tenant_count,
        }

        return Response(dashboard_data, status=status.HTTP_200_OK)
