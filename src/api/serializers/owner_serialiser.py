from owner.models.owner_model import OwnerModel
from rest_framework.serializers import ModelSerializer
from owner.models.folder_model import FolderModel
from .folder_serializer import FolderSerializer


class OwnerSerializer(ModelSerializer):
    folders = FolderSerializer(many=True)

    class Meta:
        model = OwnerModel
        fields = ['id', 'password', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'cards_type',
                  'num_cni', 'image_recto', 'image_verso', 'folders']

    def create(self, validated_data):
        folders_data = validated_data.pop('folders')
        owner_instance = OwnerModel.objects.create(**validated_data)
        for char_data in folders_data:
            FolderModel.objects.create(owner=owner_instance, **char_data)
        return owner_instance

    def update(self, instance, validated_data):
        folders_data = validated_data.pop('folders', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if folders_data is not None:
            instance.folders.all().delete()
            for char_data in folders_data:
                FolderModel.objects.create(owner=instance, **char_data)

        return instance
