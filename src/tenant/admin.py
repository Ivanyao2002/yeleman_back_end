from django.contrib import admin
from .models import tenant_model


# Register your models here.

class TenantAdmin(admin.ModelAdmin):
    pass


admin.site.register(tenant_model.TenantModel, TenantAdmin)
