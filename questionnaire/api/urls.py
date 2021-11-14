from django.urls import path
from .views import SurveyDetalsView, SurveyListView, AnswerCreateView, AnswerView


urlpatterns = [
    path('survey/', SurveyListView.as_view()),
    path('survey/<int:pk>/', SurveyDetalsView.as_view()),
    path('answer/', AnswerView.as_view()),
    path('answer/create/', AnswerCreateView.as_view({'post':'create'}))
]