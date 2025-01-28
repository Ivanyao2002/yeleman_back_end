from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class ProfileViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def retrieve(self, request):
        user = request.user
        if user.is_anonymous:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        return Response({
            'username': user.username,
            'firstName': user.first_name,
            'lastName': user.last_name,
            'email': user.email,
            'phoneNumber': user.phone_number,
            'cardType': user.cards_type,
            'num_cni': user.num_cni,
            'avatar': user.avatar.url if user.avatar else None,
            'image_recto': user.image_recto.url if user.image_recto else None,
            'image_verso': user.image_verso.url if user.image_verso else None,
        }, status=status.HTTP_200_OK)

