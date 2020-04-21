from django.urls import path
from .controller import api

urlpatterns = [
   path(r"vendors/", api.vendors, name="chained_selects_vendors"),
   path(r"models/", api.models_by_vendor_id, name="chained_selects_models")
]