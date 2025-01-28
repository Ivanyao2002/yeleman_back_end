from rest_framework import serializers
from property.models.comment_model import CommentModel

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = '__all__'