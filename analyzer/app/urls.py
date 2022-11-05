from django.urls import path

from . import views

urlpatterns = [
    path("keyword/", views.KeywordAPIView.as_view()),
    path("ner/", views.NERExtractionAPIView.as_view()),
    path("sentiment/", views.SentimentAPIView.as_view()),
    path("classification/", views.ClassificationAPIView.as_view()),
]
