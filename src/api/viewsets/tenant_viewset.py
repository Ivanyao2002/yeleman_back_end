from rest_framework import viewsets, mixins
from tenant.models.tenant_model import TenantModel
from ..serializers.tenant_serialiser import TenantSerializer


class TenantViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    queryset = TenantModel.objects.filter(user__is_active=True, user__user_type='LOCATAIRE')
    serializer_class = TenantSerializer
