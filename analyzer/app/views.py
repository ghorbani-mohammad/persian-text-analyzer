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
            print(entities)
            return Response(entities)
        return Response()
