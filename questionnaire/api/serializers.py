from rest_framework import serializers
from .models import Question, Survey, User

class QuestionSerializer(serializers.ModelSerializer):
    '''Вывод вопроса'''

    class Meta:
        model = Question
        fields = ('text_question', 'attachment')

class UserSerializer(serializers.ModelSerializer):
    '''Вывод вопроса'''

    class Meta:
        model = User
        fields = ('id', 'user_name')

class SurveySerializer(serializers.ModelSerializer):
    '''Вывод вопроса'''

    class Meta:
        model = Survey
        fields = ('name', 'date_start', 'date_finish', 'description')
