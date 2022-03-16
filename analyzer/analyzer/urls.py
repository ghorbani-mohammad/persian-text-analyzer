from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('secret-admin/', admin.site.urls),
    path("v1/app/", include("app.urls")),
]
