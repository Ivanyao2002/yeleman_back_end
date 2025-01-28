from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from property.models.image_model import ImageModel
from property.models.property_model import PropertyModel
from api.serializers.property.image_serializer import ImageSerializer
from api.permissions.is_owner_permission import IsOwnerPermission


class ImageViewSet(viewsets.ModelViewSet):
    queryset = ImageModel.objects.filter(status=True)
    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    permission_classes = [AllowAny]


    def create(self, request, *args, **kwargs):
        property_id = request.data.get('property')
        images = request.FILES.getlist('image')

        if not property_id or not images:
            return Response({'error': 'Images et propriété réquis.'}, status=status.HTTP_400_BAD_REQUEST)

        property_instance = PropertyModel.objects.filter(id=property_id).first()
        if not property_instance:
            return Response({'error': 'Propriété non trouvée.'}, status=status.HTTP_404_NOT_FOUND)

        response_data = []
        for image in images:
            image_instance = ImageModel.objects.create(property=property_instance, image=image)
            response_data.append(ImageSerializer(image_instance).data)

        return Response(response_data, status=status.HTTP_201_CREATED)