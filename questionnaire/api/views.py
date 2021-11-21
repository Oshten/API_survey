
from rest_framework import generics, permissions

from .models import Survey, Question, Answer
from .permissions import SurveyPermission
from .serializers import (
    SurveyDetalsSerializer,
    SurveyListSerializer,
    QuestionListSerializer,
    CreateAnswersForSurveySerializer,
    AnswerSerializer,
    AddUserSerializer
)


class SurveyListView(generics.ListCreateAPIView):
    """Вывод опросов"""

    serializer_class = SurveyListSerializer
    permission_classes = [SurveyPermission]

    def get_queryset(self):
        surveys = Survey.objects.all()
        return surveys



class SurveyDetalsView(generics.RetrieveUpdateDestroyAPIView):
    '''Вывод деталей опроса с вопросами'''

    queryset = Survey.objects.all()
    serializer_class = SurveyDetalsSerializer


class QuestionListView(
    generics.mixins.ListModelMixin,
    generics.mixins.CreateModelMixin,
    generics.mixins.UpdateModelMixin,
    generics.mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    """Вывод вопросов одного опроса"""

    serializer_class = QuestionListSerializer
    permission_classes = [permissions.IsAdminUser]
    # lookup_url_kwarg = {'organization_slug': 'attachment'}
    lookup_field = 'attachment'

    def get_queryset(self):
        attachment = self.kwargs['attachment']
        questions = Question.objects.filter(attachment=attachment)
        return questions


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


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







