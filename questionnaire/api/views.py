
from rest_framework import viewsets, generics

from .models import Survey, Answer
from .serializers import (
    SurveyDetalsSerializer,
    SurveyListSerializer,
    AnswerCreateSerializer,
    AnswerSerializer
)


class SurveyListView(generics.ListCreateAPIView):
    """Вывод опросов"""

    serializer_class = SurveyListSerializer

    def get_queryset(self):
        surveys = Survey.objects.all()
        return surveys



class SurveyDetalsView(generics.RetrieveUpdateDestroyAPIView):
    '''Вывод деталей опроса с вопросами'''

    queryset = Survey.objects.all()
    serializer_class = SurveyDetalsSerializer


class AnswerCreateView(viewsets.ModelViewSet):
    '''Добавление ответов на вопросы'''

    serializer_class = AnswerCreateSerializer

class AnswerView(generics.ListAPIView):
    '''Вывод ответов на вопросы'''

    serializer_class = AnswerSerializer
    def get_queryset(self):
        answers = Answer.objects.all()
        return answers







