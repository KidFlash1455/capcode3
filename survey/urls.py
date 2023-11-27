from django.urls import path
from . import views
from .views import (
    SurveyListView,
    SurveyDetailView,
    SurveyUpdateView,
    SurveyDeleteView,
    SurveyCreateView,
)

urlpatterns = [
    path("", SurveyListView.as_view(), name="survey_list"),
    path("<int:pk>/", SurveyDetailView.as_view(), name="survey_detail"),
    path("<int:pk>/edit/", SurveyUpdateView.as_view(), name="survey_edit"),
    path("<int:pk>/delete/", SurveyDeleteView.as_view(), name="survey_delete"),
    path("new/", SurveyCreateView.as_view(), name="survey_new"),
    path("survey_pdf/", views.survey_pdf, name="survey_pdf"),
]
