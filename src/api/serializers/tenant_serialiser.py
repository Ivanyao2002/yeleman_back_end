from tenant.models.tenant_model import TenantModel
from rest_framework.serializers import ModelSerializer


class TenantSerializer(ModelSerializer):
    class Meta:
        model = TenantModel
        fields = ['id', 'user']
        depth = 2
