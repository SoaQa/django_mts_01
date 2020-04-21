from django.urls import path
from .controller import api

urlpatterns = [
   path(r"vendors/", api.vendors, name="chained_selects_vendors"),
   path(r"devices/<int:vendor_id>", api.devices_by_vendor_id, name="chained_selects_models"),
   path(r"firmwares/<int:device_id>", api.firmwares_by_device_id, name="chained_selects_firmwares"),
]