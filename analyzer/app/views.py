from rest_framework import views
from rest_framework.response import Response

class NERExtractionAPIView(views.APIView):
    def post(self, request):
        return Response({"keywords": "keywords", "keyphrases": "keyphrases"})
