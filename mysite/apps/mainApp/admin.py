from django.contrib import admin
from .models import Vendor, Device, FirmwareVersion
# Register your models here.


class MainAdmin(admin.ModelAdmin):
    readonly_fields = ['id', ]


admin.site.register(Vendor, MainAdmin)
admin.site.register(Device, MainAdmin)
admin.site.register(FirmwareVersion, MainAdmin)
