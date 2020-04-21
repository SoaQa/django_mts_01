from django.http import JsonResponse, HttpResponse
from mysite.apps.api.models import Vendor, Device, FirmwareVersion


def vendors(request):
    vendors_dict = [{'id': i.id, 'name': i.name} for i in Vendor.objects.all()]
    return JsonResponse(vendors_dict, safe=False)


def devices_by_vendor_id(request):
    if 'VendorID' not in request.headers:
        return HttpResponse(content='<h1>Header - VendorID does not exists!</h1>', status=400,
                            content_type="text/html; charset=utf-8")

    models_dict = [{'id': i.id, 'name': i.name, 'vendor_id': i.vendor_id} for i in
                   Device.objects.filter(vendor_id=request.headers['VendorID'])]
    return JsonResponse(models_dict, safe=False)


def firmwares_by_model_id(request):
    if 'DeviceID' not in request.headers:
        return HttpResponse(content='<h1>Header - DeviceID does not exists!</h1>', status=400,
                            content_type="text/html; charset=utf-8")

    firmwares_dict = [{'id': i.id, 'name': i.version, 'device_id': i.device_id} for i in
                   FirmwareVersion.objects.filter(device_id=request.headers['DeviceID'])]
    return JsonResponse(firmwares_dict, safe=False)
