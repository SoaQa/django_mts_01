from django.shortcuts import render

# class for methods for js


def index(request):
    return render(request, "main/select.html")
