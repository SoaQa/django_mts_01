from django.urls import path
from .controller import views
from ..api.controller import api

urlpatterns = [
   path(r"", views.index, name="index"),
   path(r"api/vendors", api.vendors, name="chained_selects_data")
]