from django.urls import path
from .views import (
    SurveyDetalsView,
    SurveyListView,
    QuestionListView,
    QuestionDetalsView,
    AddAnswersView,
    AnswerForSurveyDetalsView,
    AddUserView)




urlpatterns = [
    path('survey/', SurveyListView.as_view()),
    path('survey/<int:pk>/', SurveyDetalsView.as_view()),
    path('survey/<int:attachment>/questions/', QuestionListView.as_view()),
    path('survey/<int:attachment>/questions/<int:pk>/', QuestionDetalsView.as_view()),
    path('user/', AddUserView.as_view()),
    path('answer/', AddAnswersView.as_view()),
    path('answer/<int:pk>/', AnswerForSurveyDetalsView.as_view()),
]

