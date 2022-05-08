import logging
import traceback

from rest_framework import views
from rest_framework.response import Response

from . import apps, utils
from .rake import get_text_keywords

logger = logging.getLogger(__name__)


class NERExtractionAPIView(views.APIView):
    def post(self, request):
        text = request.data["text"]
        try:
            ner_output = apps.AppConfig.ner_model(
                apps.AppConfig.normalizer.normalize(text)
            )
            if len(ner_output) > 0:
                entities = utils.ner_report(ner_output)
                return Response(entities)
        except:
            logger.error(traceback.format_exc())
        return Response({})


class SentimentAPIView(views.APIView):
    def post(self, request):
        text = request.data["text"]
        try:
            result = apps.AppConfig.sentiment_model(
                apps.AppConfig.normalizer.normalize(text), return_all_scores=True
            )[0]
            temp = {
                "angry": result[0]["score"] + result[1]["score"],
                "happy": result[3]["score"] + result[4]["score"],
                "neutral": result[2]["score"],
            }
            return Response(temp)
        except:
            logger.error(traceback.format_exc())
        return Response({})


class ClassificationAPIView(views.APIView):
    def post(self, request):
        text = request.data["text"]
        try:
            result = apps.AppConfig.classification_model(
                apps.AppConfig.normalizer.normalize(text), return_all_scores=True
            )[0]
            return Response(result)
        except:
            logger.error(traceback.format_exc())
        return Response({})


class KeywordAPIView(views.APIView):
    def post(self, request):
        text = request.data["text"]
        kw, kp = get_text_keywords(text)
        return Response({"keywords": kw, "keyphrases": kp})
