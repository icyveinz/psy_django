from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.models import StudyResultsCard
from wagtail_landing.serializers import StudyResultsCardSerializer


# Create your views here.


@api_view(["GET"])
def study_results_api(request):
    cards = StudyResultsCard.objects.all()
    serializer = StudyResultsCardSerializer(cards, many=True)
    return Response(serializer.data)
