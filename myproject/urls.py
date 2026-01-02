from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),          # Django admin
    path("api/", include("myapp.urls")),      # App-level URLs ko /api/ ke under expose karenge
]
