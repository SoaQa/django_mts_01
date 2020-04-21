from django.urls import path
from . import views

urlpatterns = [
   path(r"", views.index, name="index"),
   path(r"vendor_model_firmware/", views.get_vendor_model_firmware, name="chained_selects_data")
]