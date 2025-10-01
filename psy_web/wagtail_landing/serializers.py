from rest_framework import serializers
from core.models import StudyResultsLink, StudyResultsCard

class StudyResultsLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyResultsLink
        fields = ['skills_achieved']

class StudyResultsCardSerializer(serializers.ModelSerializer):
    study_results_li = StudyResultsLinkSerializer(many=True, read_only=True)

    class Meta:
        model = StudyResultsCard
        fields = ['course_title', 'course_platform', 'year_ended', 'study_results_li']