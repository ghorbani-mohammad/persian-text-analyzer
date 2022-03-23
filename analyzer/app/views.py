from rest_framework import views
from rest_framework.response import Response

from . import apps
from . import utils

class NERExtractionAPIView(views.APIView):
    def post(self, request):
        text = request.data['text']
        ner_output = apps.AppConfig.ner_model(apps.AppConfig.normalizer.normalize(text))
        if len(ner_output) > 0:
            entities = utils.ner_report(ner_output)
            return Response(entities)
        return Response()

class SentimentAPIView(views.APIView):
    def post(self, request):
        text = request.data['text']
        result = apps.AppConfig.sentiment_model(apps.AppConfig.normalizer.normalize(text), return_all_scores=True)
        return Response(result[0])


class ClassificationAPIView(views.APIView):
    def post(self, request):
        text = request.data['text']
        result = apps.AppConfig.classification_model(apps.AppConfig.normalizer.normalize(text))
        return Response(result)
