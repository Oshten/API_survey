from django.urls import path
from .views import (
    SurveyDetalsView,
    SurveyListView,
    QuestionListView,
    AddAnswersView,
    AnswerView,
    AddUserView)




urlpatterns = [
    path('survey/', SurveyListView.as_view()),
    path('survey/<int:pk>/', SurveyDetalsView.as_view()),
    path('survey/<int:attachment>/questions/', QuestionListView.as_view()),
    path('answer/', AddUserView.as_view())
]

