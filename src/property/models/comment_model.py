from django.db import models
from base.models.helpers.date_time_model import DateTimeModel


class CommentModel(DateTimeModel):

    property = models.ForeignKey("property.PropertyModel", on_delete=models.CASCADE, related_name="comment_property_id")
    content = models.TextField(verbose_name="Commentaire ")
    note = models.IntegerField(verbose_name="Note ")

    def __str__(self):
        return f"{self.content} - {self.note}"

    class Meta:
        verbose_name = "Commentaire"
        verbose_name_plural = "Commentaires"
