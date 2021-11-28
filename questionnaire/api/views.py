
from rest_framework import generics, permissions, status

from .models import Survey, Question, Result, Answer, User
from .permissions import SurveyPermission
from .serializers import (
    SurveyDetalsSerializer,
    SurveyListSerializer,
    QuestionSerializer,
    # QuestionListSerializer,
    CreateResultSerializer,
    ResultDetalsSerializer,
    # CreateAnswerSerializer,
    AnswersListSerializer,
    AnswerDetalsSerializer,
    AddUserSerializer,
    AllUsersAndResultsSerializer
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
    permission_classes = [SurveyPermission]

class QuestionListView(
    generics.mixins.ListModelMixin,
    generics.mixins.CreateModelMixin,
    generics.mixins.DestroyModelMixin,
    generics.GenericAPIView):
    """Вывод вопросов одного опроса"""

    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        attachment = self.kwargs['attachment']
        questions = Question.objects.filter(attachment=attachment)
        return questions

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class QuestionDetalsView(generics.RetrieveUpdateDestroyAPIView):
    """Вывод вопроса для редактирования и удаления"""

    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        attachment = self.kwargs['attachment']
        question = Question.objects.filter(attachment=attachment)
        return question



class AddResultView(generics.ListCreateAPIView):
    '''Добавление ответов на опросы'''

    serializer_class = CreateResultSerializer
    queryset = Result.objects.all()

class AddAnswerView(generics.ListCreateAPIView):
    '''Добавление ответов'''

    serializer_class = AnswersListSerializer

    def get_queryset(self):
        answers_for_survey = self.kwargs['answers_for_survey']
        answers = Answer.objects.filter(answers_for_survey=answers_for_survey)
        return answers


class ResultDetalsView(generics.RetrieveAPIView):
    '''Вывод деталей опроса с вопросами'''

    serializer_class = ResultDetalsSerializer
    queryset = Result.objects.all()

class AnswerDetalsView(generics.RetrieveUpdateDestroyAPIView):
    '''Вывод деталей, редактирование и удаление ответа'''

    serializer_class = AnswerDetalsSerializer

    def get_queryset(self):
        answers_for_survey = self.kwargs['answers_for_survey']
        answer = Answer.objects.filter(answers_for_survey=answers_for_survey)
        return answer



class AddUserView(generics.CreateAPIView):
    '''Добавление пользователя'''

    serializer_class = AddUserSerializer
    queryset = User.objects.all()

class AllUsersAndResultsView(generics.ListAPIView):
    '''Вывод всех пользователей и их ответы'''

    serializer_class = AllUsersAndResultsSerializer
    permission_classes = [permissions.IsAdminUser,]
    queryset = User.objects.all()









