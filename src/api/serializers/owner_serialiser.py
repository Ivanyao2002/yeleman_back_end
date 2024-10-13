from owner.models.owner_model import OwnerModel
from rest_framework.serializers import ModelSerializer


class OwnerSerializer(ModelSerializer):
    class Meta:
        model = OwnerModel
        fields = ['id', 'password', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'cards_type',
                  'num_cni', 'image_recto', 'image_verso']
