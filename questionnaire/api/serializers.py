from rest_framework import serializers
from .models import Question, Survey, User, AnswersForSurvey, Answer


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
    questions = QuestionSerializer(read_only=True, many=True)

    class Meta:
        model = Survey
        fields = ('id', 'survey_name', 'description', 'questions')



class SurveySerializer(serializers.ModelSerializer):
    '''Вывод опроса с вопросами'''

    class Meta:
        model = Survey
        fields = ('id', 'survey_name', 'description')



class SurveyListSerializer(serializers.ModelSerializer):
    """Список опросов"""

    class Meta:
        model = Survey
        fields = ('id', 'survey_name', 'description')

class CreateAnswersForSurveySerializer(serializers.ModelSerializer):
    '''Добавление ответов на опрос'''

    class Meta:
        model = AnswersForSurvey
        fields = '__all__'

    def create(self, validated_data):
        answer_for_survey = AnswersForSurvey.objects.update_or_create(
            survey_parent=validated_data.get('survey_parent', None),
            user_answers=validated_data.get('user_answers', None)
        )
        return answer_for_survey


class AnswerSerializer(serializers.ModelSerializer):
    '''Вывод ответов на вопросы'''
    answer = QuestionSerializer()
    user_answer = UserSerializer()

    class Meta:
        model = Answer
        fields = ('__all__')


class AddUserSerializer(serializers.ModelSerializer):
    '''Добавление пользователя'''
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user_name = User.objects.create(
            user_name=validated_data.get('user_name', None)
        )

