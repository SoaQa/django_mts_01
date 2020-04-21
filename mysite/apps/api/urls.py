from django.urls import path
from .controller import api

urlpatterns = [
   path(r"vendors/", api.vendors, name="chained_selects_vendors"),
   path(r"models/", api.devices_by_vendor_id, name="chained_selects_models"),
   path(r"firmwares/", api.firmwares_by_model_id, name="chained_selects_firmwares"),
]