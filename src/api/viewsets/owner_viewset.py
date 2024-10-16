from rest_framework import mixins, viewsets
from owner.models.owner_model import OwnerModel
from ..serializers.owner_serialiser import OwnerSerializer


class OwnerViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    queryset = OwnerModel.objects.filter(user__is_active=True, user__user_type='PROPRIETAIRE')
    serializer_class = OwnerSerializer
