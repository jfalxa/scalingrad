from django.http import JsonResponse


def root(_):
    return JsonResponse({"message": "Welcome"})
