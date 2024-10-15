from rest_framework import serializers
from owner.models.folder_model import FolderModel


class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = FolderModel
        fields = ['id', 'acd_number', 'property_type', 'localization']
