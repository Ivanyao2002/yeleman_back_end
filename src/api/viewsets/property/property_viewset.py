from rest_framework import viewsets
from api.serializers.property.property_serializer import PropertySerializer
from property.models.property_model import PropertyModel


class PropertyViewSet(viewsets.ModelViewSet):
    serializer_class = PropertySerializer
    queryset = PropertyModel.objects.filter(status=True)
