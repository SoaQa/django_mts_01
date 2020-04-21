from django.http import JsonResponse, HttpResponse
from mysite.apps.api.models import Vendor, Device, FirmwareVersion


def vendors(request):
    vendors_dict = [{'id': i.id, 'name': i.name} for i in Vendor.objects.all()]
    return JsonResponse(vendors_dict, safe=False)


def devices_by_vendor_id(request, vendor_id):
    models_dict = [{'id': i.id, 'name': i.name, 'vendor_id': i.vendor_id} for i in
                   Device.objects.filter(vendor_id=vendor_id)]
    return JsonResponse(models_dict, safe=False)


def firmwares_by_device_id(request, device_id):
    firmwares_dict = [{'id': i.id, 'name': i.version, 'device_id': i.device_id} for i in
                   FirmwareVersion.objects.filter(device_id=device_id)]
    return JsonResponse(firmwares_dict, safe=False)
