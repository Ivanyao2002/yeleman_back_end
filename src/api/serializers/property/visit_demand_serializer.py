from property.models.demand_model import DemandModel
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, SerializerMethodField
from property.models.property_model import PropertyModel


class VisitDemandSerializer(ModelSerializer):
    property = PrimaryKeyRelatedField(queryset=PropertyModel.objects.filter(status=True, state='Disponible'))
    property_details = SerializerMethodField()

    def get_property_details(self, obj):

        return {
            'name': obj.property.label,
        }

    class Meta:
        model = DemandModel
        fields = ['id', 'property', 'visit_date', 'comment', 'demand_status', 'tenant', 'property_details']
        depth = 2
        extra_kwargs = {
            'property': {
              'write_only': True
            },
            'tenant': {
                'read_only': True
            },
        }
