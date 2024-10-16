from django.contrib import admin
from .models import demand_model, property_model


# Register your models here.

class PropertyAdmin(admin.ModelAdmin):
    pass


class DemandAdmin(admin.ModelAdmin):
    pass


admin.site.register(demand_model.DemandModel, DemandAdmin)
admin.site.register(property_model.PropertyModel, PropertyAdmin)
