import logging

from rest_framework import views
from rest_framework.response import Response

from . import apps, utils
from .rake import get_text_keywords

logger = logging.getLogger(__name__)


class NERExtractionAPIView(views.APIView):
    def post(self, request):
        text = request.data["text"]
        ner_output = apps.AppConfig.ner_model(apps.AppConfig.normalizer.normalize(text))
        if len(ner_output) > 0:
            entities = utils.ner_report(ner_output)
            return Response(entities)
        return Response({})


class SentimentAPIView(views.APIView):
    def post(self, request):
        text = request.data["text"]
        try:
            result = apps.AppConfig.sentiment_model(
                apps.AppConfig.normalizer.normalize(text), return_all_scores=True
            )[0]
        except Exception as e:
            logger.error(e)
            return {}
        temp = {
            "angry": result[0]["score"] + result[1]["score"],
            "happy": result[3]["score"] + result[4]["score"],
            "neutral": result[2]["score"],
        }
        return Response(temp)


class ClassificationAPIView(views.APIView):
    def post(self, request):
        text = request.data["text"]
        try:
            result = apps.AppConfig.classification_model(
                apps.AppConfig.normalizer.normalize(text), return_all_scores=True
            )[0]
        except Exception as e:
            logger.error(e)
            return {}
        return Response(result)


class KeywordAPIView(views.APIView):
    def post(self, request):
        text = request.data["text"]
        kw, kp = get_text_keywords(text)
        return Response({"keywords": kw, "keyphrases": kp})
