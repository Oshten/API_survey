from rest_framework import serializers
from .models import Question, Survey, User, Answer


class QuestionSerializer(serializers.ModelSerializer):
    '''Вывод вопросов'''

    class Meta:
        model = Question
        fields = ('text_question',)

class UserSerializer(serializers.ModelSerializer):
    '''Вывод вопроса'''

    class Meta:
        model = User
        fields = ('id', 'user_name')

class SurveyDetalsSerializer(serializers.ModelSerializer):
    '''Вывод опроса с вопросами'''
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Survey
        fields = ('id', 'name', 'description', 'questions')


class SurveySerializer(serializers.ModelSerializer):
    '''Вывод опроса с вопросами'''

    class Meta:
        model = Survey
        fields = ('id', 'name', 'description')


class SurveyListSerializer(serializers.ModelSerializer):
    """Список опросов"""

    class Meta:
        model = Survey
        fields = ('id', 'name', 'description')

class AnswerCreateSerializer(serializers.ModelSerializer):
    '''Добавление ответов на вопросы'''

    class Meta:
        model = Answer
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    '''Вывод ответов на вопросы'''
    answer = QuestionSerializer()
    user_answer = UserSerializer()

    class Meta:
        model = Answer
        fields = ('__all__')