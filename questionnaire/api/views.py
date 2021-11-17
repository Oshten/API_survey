
from rest_framework import generics, permissions

from .models import Survey, Answer
from .permissions import SurveyPermission
from .serializers import (
    SurveyDetalsSerializer,
    SurveyListSerializer,
    CreateAnswersForSurveySerializer,
    AnswerSerializer,
    AddUserSerializer
)


class SurveyListView(generics.ListCreateAPIView):
    """Вывод опросов"""

    queryset = Survey.objects.all()
    serializer_class = SurveyListSerializer
    permission_classes = [SurveyPermission]

    # def get_queryset(self):
    #     surveys = Survey.objects.all()
    #     return surveys



class SurveyDetalsView(generics.RetrieveUpdateDestroyAPIView):
    '''Вывод деталей опроса с вопросами'''

    queryset = Survey.objects.all()
    serializer_class = SurveyDetalsSerializer


class AddAnswersView(generics.CreateAPIView):
    '''Добавление ответов на опросы'''

    serializer_class = CreateAnswersForSurveySerializer

class AddUserView(generics.CreateAPIView):
    '''Добавление пользователя'''

    serializer_class = AddUserSerializer



class AnswerView(generics.ListAPIView):
    '''Вывод ответов на вопросы'''

    serializer_class = AnswerSerializer
    def get_queryset(self):
        answers = Answer.objects.all()
        return answers







