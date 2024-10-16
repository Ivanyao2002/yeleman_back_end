from django.db import models
from base.models.helpers.date_time_model import DateTimeModel
from base.models.payment_type_enum import PaymentTypeEnum


class PaymentModel(DateTimeModel):
    user = models.ForeignKey("user.CustomUserModel", on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=20, choices=PaymentTypeEnum.choices,
                                    default=PaymentTypeEnum.SUBSCIPTION, verbose_name="Type de paiement ")

    def __str__(self):
        return f"{self.payment_type}"

    class Meta:
        verbose_name = "Paiement"
        verbose_name_plural = "Paiements"
