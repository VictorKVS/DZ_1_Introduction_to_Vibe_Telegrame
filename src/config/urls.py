from django.contrib import admin
from django.http import JsonResponse
from django.urls import path


def health(_: object) -> JsonResponse:
    return JsonResponse({"service": "father", "status": "ok"})


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/health/", health, name="health"),
]
