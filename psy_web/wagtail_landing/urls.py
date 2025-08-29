from django.urls import path
from wagtail_landing.views import study_results_api

urlpatterns = [
    path('api/study-results/', study_results_api, name='study-results-api'),
]