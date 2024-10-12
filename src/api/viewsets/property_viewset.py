from rest_framework import viewsets
from api.serializers.property_serializer import PropertySerializer
from property.models.property_model import PropertyModel
from rest_framework.permissions import IsAuthenticated




class PropertyViewset(viewsets.ModelViewSet):
    serializer_class= PropertySerializer
    queryset = PropertyModel.objects.all()
    permission_classes = [IsAuthenticated]