
from rest_framework import generics, permissions, status

from .models import Survey, Question, AnswersForSurvey, Answer, User
from .permissions import SurveyPermission
from .serializers import (
    SurveyDetalsSerializer,
    SurveyListSerializer,
    QuestionListSerializer,
    CreateAnswersForSurveySerializer,
    AnswerForSurveyDetalsSerializer,
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
    permission_classes = [SurveyPermission]

class QuestionListView(
    generics.mixins.ListModelMixin,
    generics.mixins.CreateModelMixin,
    generics.mixins.DestroyModelMixin,
    generics.GenericAPIView):
    """Вывод вопросов одного опроса"""

    serializer_class = QuestionListSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        attachment = self.kwargs['attachment']
        questions = Question.objects.filter(attachment=attachment)
        return questions

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # def perform_create(self, serializer):
    #     serializer.save(attachment=models.Count(Survey, ip=self.kwargs["attachment"]))

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class QuestionDetalsView(generics.RetrieveUpdateDestroyAPIView):
    """Вывод вопроса для редактирования и удаления"""

    serializer_class = QuestionListSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        attachment = self.kwargs['attachment']
        question = Question.objects.filter(attachment=attachment)
        return question



class AddAnswersView(generics.ListCreateAPIView):
    '''Добавление ответов на опросы'''

    serializer_class = CreateAnswersForSurveySerializer
    queryset = AnswersForSurvey.objects.all()


class AnswerForSurveyDetalsView(
    generics.mixins.CreateModelMixin,
    generics.mixins.RetrieveModelMixin,
    generics.mixins.DestroyModelMixin,
    generics.GenericAPIView):
    '''Вывод деталей опроса с вопросами'''

    serializer_class = AnswerForSurveyDetalsSerializer
    queryset = AnswersForSurvey.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class AddUserView(generics.CreateAPIView):
    '''Добавление пользователя'''

    serializer_class = AddUserSerializer
    queryset = User.objects.all()





# class AnswerView(generics.ListAPIView):
#     '''Вывод ответов на вопросы'''
#
#     serializer_class = AnswerSerializer
#     def get_queryset(self):
#         answers = Answer.objects.all()
#         return answers







