from django.contrib import admin
from .models import owner_model, folder_model


# Register your models here.

class OwnerAdmin(admin.ModelAdmin):
    pass


class FolderAdmin(admin.ModelAdmin):
    pass


admin.site.register(owner_model.OwnerModel, OwnerAdmin)
admin.site.register(folder_model.FolderModel, FolderAdmin)
