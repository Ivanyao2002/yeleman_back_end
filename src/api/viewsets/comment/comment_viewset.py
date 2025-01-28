from rest_framework import viewsets
from property.models.comment_model import CommentModel
from api.serializers.comment.comment_serializer import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer