from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "dist/index.html")


def root(_) -> JsonResponse:
    return JsonResponse({"message": "Welcome"})
