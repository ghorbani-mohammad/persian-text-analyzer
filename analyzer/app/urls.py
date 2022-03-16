
from django.urls import path

from . import views

urlpatterns = [
    path("ner/", views.NERExtractionAPIView.as_view()),
]