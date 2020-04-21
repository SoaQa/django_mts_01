from django.http import JsonResponse, HttpResponse
from mysite.apps.api.models import *


def vendors(request):
    vendors_dict = [{'id': i.id, 'name': i.name} for i in Vendor.objects.all()]
    return JsonResponse(vendors_dict, safe=False)


def models_by_vendor_id(request):
    if 'VendorID' not in request.headers:
        return HttpResponse(content='<h1>VendorID does not exists!</h1>', status=400)
    return HttpResponse(request.headers['VendorID'])

