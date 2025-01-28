from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from property.models.property_model import PropertyModel
from owner.models.owner_model import OwnerModel
from api.serializers.property.property_serializer import PropertySerializer
from api.permissions.is_owner_permission import IsOwnerPermission
from rest_framework.exceptions import NotFound


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = PropertyModel.objects.filter(status=True)
    serializer_class = PropertySerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsOwnerPermission]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['owner'] = OwnerModel.objects.get(user=request.user)
            serializer.validated_data['status'] = False
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'], url_path='filter', permission_classes=[AllowAny])
    def filter_properties(self, request):
        queryset = self.queryset

        price = request.query_params.get('price', None)
        if price is not None:
            queryset = queryset.filter(price=price)

        property_type = request.query_params.get('property_type', None)
        if property_type is not None:
            property_type_list = property_type.split(',')
            queryset = queryset.filter(property_type__in=property_type_list)

        address = request.query_params.get('address', None)
        if address is not None:
            address_list = address.split(',')
            queryset = queryset.filter(address__in=address_list)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_property_by_owner(self, request, slug=None):
        try:
            property_instance = PropertyModel.objects.get(slug=slug, owner=OwnerModel.objects.get(user=request.user))
            serializer = self.get_serializer(property_instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except PropertyModel.DoesNotExist:
            raise NotFound(detail="Propriété non trouvée.")

    def retrieve(self, request, slug=None, *args, **kwargs):
        try:
            property_instance = PropertyModel.objects.get(slug=slug)
            serializer = self.get_serializer(property_instance)
            return Response(serializer.data)
        except PropertyModel.DoesNotExist:
            raise NotFound(detail="Propriété non trouvée.")

    def update(self, request, slug=None, *args, **kwargs):
        try:
            instance = PropertyModel.objects.get(slug=slug, owner=OwnerModel.objects.get(user=request.user))
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except PropertyModel.DoesNotExist:
            raise NotFound(detail="Propriété non trouvée.")

    def destroy(self, request, slug=None, *args, **kwargs):
        try:
            instance = PropertyModel.objects.get(slug=slug, owner=OwnerModel.objects.get(user=request.user))
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except PropertyModel.DoesNotExist:
            raise NotFound(detail="Propriété non trouvée.")

    @action(detail=False, methods=['get'], url_path='owner-properties', permission_classes=[IsOwnerPermission])
    def list_properties_by_owner(self, request):
        owner = OwnerModel.objects.get(user=request.user)
        queryset = PropertyModel.objects.filter(owner=owner)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
