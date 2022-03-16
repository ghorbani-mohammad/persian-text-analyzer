from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('secret_admin/', admin.site.urls),
    path("ner/", views.NERExtractionAPIView.as_view()),
]
