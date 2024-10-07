from django.db import models
from .helpers.date_time_model import DateTimeModel


class MessageModel(DateTimeModel):
    tenant = models.ForeignKey("tenant.TenantModel", on_delete=models.CASCADE)
    content = models.TextField(verbose_name="Description ")

    def __str__(self):
        return f"{self.content}"

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
