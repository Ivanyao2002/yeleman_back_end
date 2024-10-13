from tenant.models.tenant_model import TenantModel
from rest_framework.serializers import ModelSerializer


class TenantSerializer(ModelSerializer):
    class Meta:
        model = TenantModel
        fields = ['id', 'password', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'cards_type',
                  'num_cni', 'image_recto', 'image_verso']
