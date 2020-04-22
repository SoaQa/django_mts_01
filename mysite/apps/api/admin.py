from django.contrib import admin

# Register your models here.
from mysite.apps.api.models import Vendor, Device, FirmwareVersion, Firmware


class MainAdmin(admin.ModelAdmin):
    readonly_fields = ['id', ]


admin.site.register(Vendor, MainAdmin)
admin.site.register(Device, MainAdmin)
admin.site.register(FirmwareVersion, MainAdmin)
admin.site.register(Firmware, MainAdmin)
