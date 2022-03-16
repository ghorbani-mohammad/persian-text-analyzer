from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('secret_admin/', admin.site.urls),
]
