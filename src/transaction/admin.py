from django.contrib import admin
from .models import subscription_model, subscription_plan_model, payment_model, historic_model


# Register your models here.

class SubscriptionPlanAdmin(admin.ModelAdmin):
    pass


class SubscriptionAdmin(admin.ModelAdmin):
    pass


class PaymentAdmin(admin.ModelAdmin):
    pass


class HistoricAdmin(admin.ModelAdmin):
    pass


admin.site.register(subscription_plan_model.SubscriptionPlanModel, SubscriptionPlanAdmin)
admin.site.register(subscription_model.SubscriptionModel, SubscriptionAdmin)
admin.site.register(payment_model.PaymentModel, PaymentAdmin)
admin.site.register(historic_model.HistoricModel, HistoricAdmin)
