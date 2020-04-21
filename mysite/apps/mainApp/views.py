from django.http import JsonResponse
from django.shortcuts import render
import json

# class for methods for js

params_array = [
 {
  "id":"1",
  "name":"Huawei",
  "parent_id":"0"
 },
 {
  "id":"2",
  "name":"Nokia",
  "parent_id":"0"
 },
 {
  "id":"3",
  "name":"Cisco",
  "parent_id":"0"
 },
 {
  "id":"4",
  "name":"atn910c",
  "parent_id":"1"
 },
 {
  "id":"5",
  "name":"cx600-x1",
  "parent_id":"1"
 },
 {
  "id":"6",
  "name":"sr7750",
  "parent_id":"2"
 },
 {
  "id":"7",
  "name":"sas7210",
  "parent_id":"2"
 },
 {
  "id":"8",
  "name":"asr9000",
  "parent_id":"3"
 },
 {
  "id":"9",
  "name":"7600",
  "parent_id":"3"
 },
 {
  "id":"10",
  "name":"atn910c firmware 1",
  "parent_id":"4"
 },
 {
  "id":"11",
  "name":"atn910c firmware 2",
  "parent_id":"4"
 },
 {
  "id":"12",
  "name":"atn910c firmware 3",
  "parent_id":"4"
 },
 {
  "id":"13",
  "name":"cx600-x1 firmware 1",
  "parent_id":"5"
 },
 {
  "id":"14",
  "name":"cx600-x1 firmware 2",
  "parent_id":"5"
 },
 {
  "id":"15",
  "name":"cx600-x1 firmware 3",
  "parent_id":"5"
 },
 {
  "id":"17",
  "name":"sr7750 frimware 1",
  "parent_id":"6"
 },
 {
  "id":"18",
  "name":"sr7750 frimware 2",
  "parent_id":"6"
 },
 {
  "id":"19",
  "name":"sr7750 frimware 3",
  "parent_id":"6"
 },
 {
  "id":"20",
  "name":"sas7210 frimware 1",
  "parent_id":"7"
 },
 {
  "id":"21",
  "name":"sas7210 frimware 2",
  "parent_id":"7"
 },
 {
  "id":"22",
  "name":"asr9000 frimware 1",
  "parent_id":"8"
 },
 {
  "id":"23",
  "name":"asr9000 frimware 2",
  "parent_id":"8"
 },
 {
  "id":"24",
  "name":"7600 firmware 1",
  "parent_id":"9"
 },
 {
  "id":"25",
  "name":"7600 firmware 2",
  "parent_id":"9"
 }
]


def index(request):
    return render(request, "main/select.html")


def get_vendor_model_firmware(request):
    return JsonResponse(json.dumps(params_array), safe=False)