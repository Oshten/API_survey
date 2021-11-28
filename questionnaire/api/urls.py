from django.urls import path
from .views import (
    SurveyDetalsView,
    SurveyListView,
    QuestionListView,
    QuestionDetalsView,
    AddResultView,
    ResultDetalsView,
    AddAnswerView,
    AnswerDetalsView,
    AddUserView,
    AllUsersAndResultsView,
)




urlpatterns = [
    path('survey/', SurveyListView.as_view()),
    path('survey/<int:pk>/', SurveyDetalsView.as_view()),
    path('survey/<int:attachment>/questions/', QuestionListView.as_view()),
    path('survey/<int:attachment>/questions/<int:pk>/', QuestionDetalsView.as_view()),
    path('user/', AddUserView.as_view()),
    path('result/', AddResultView.as_view()),
    path('result/<int:pk>/', ResultDetalsView.as_view()),
    path('result/<int:answers_for_survey>/answers', AddAnswerView.as_view()),
    path('result/<int:answers_for_survey>/answers/<int:pk>', AnswerDetalsView.as_view()),
    path('user/result', AllUsersAndResultsView.as_view()),
]

