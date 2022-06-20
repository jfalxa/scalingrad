from django.http import JsonResponse


def root() -> JsonResponse:
    return JsonResponse({"message": "Welcome"})
