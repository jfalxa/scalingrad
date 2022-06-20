from django.http import HttpRequest, JsonResponse


def root(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"message": "Welcome"})
