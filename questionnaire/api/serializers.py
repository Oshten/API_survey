# from datetime import datetime
# from django.utils.datetime_safe import datetime
from rest_framework import serializers
from .models import Question, Survey, User, AnswersForSurvey, Answer


class UserSerializer(serializers.ModelSerializer):
    '''Вывод вопроса'''

    class Meta:
        model = User
        fields = ('id', 'ip', 'user_name',)

class QuestionSerializer(serializers.ModelSerializer):
    '''Вывод вопросов'''

    class Meta:
        model = Question
        fields = ('id', 'text_question', 'attachment')

class QuestionListSerializer(serializers.ModelSerializer):
    '''Вывод вопросов одного опроса'''

    class Meta:
        model = Question
        fields = ('__all__')




class SurveyDetalsSerializer(serializers.ModelSerializer):
    '''Вывод опроса с вопросами'''
    questions = QuestionSerializer(read_only=True, many=True)

    class Meta:
        model = Survey
        fields = ('id', 'survey_name', 'description', 'questions')



class SurveySerializer(serializers.ModelSerializer):
    '''Вывод опроса'''

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
    surwey_parent = SurveySerializer(read_only=True)
    user_answer = UserSerializer(read_only=True)

    class Meta:
        model = AnswersForSurvey
        fields = '__all__'

    # def create(self, validated_date):
    #     answers = AnswersForSurvey.objects.update_or_create(
    #         date_start_answers=str(datetime),
    #         user_answer=validated_date.get('user_answer', None),
    #         survey_parent=validated_date.get('survey_parent', None),
    #     )
    #     return answers


class CreateAnswerSerializer(serializers.ModelSerializer):
    '''Добавление и вывод ответов на вопросы'''

    class Meta:
        model = Answer
        fields = ('__all__')

    def create(self, validated_data):
        answer = Answer.objects.update_or_create(
            question_for_answer=validated_data.get('question_for_answer', None),
            answers_for_survey=validated_data.get('answers_for_survey', None),
            default={'text_answer': validated_data.get('text_answer')},
        )
        return answer


class AnswerForSurveyDetalsSerializer(serializers.ModelSerializer):
    '''Вывод деталей ответов на опросы'''
    surwey_parent = SurveyDetalsSerializer(read_only=True)
    user_answer = UserSerializer(read_only=True)
    answers_for_survey = CreateAnswerSerializer(many=True)

    class Meta:
        model = AnswersForSurvey
        fields = ('surwey_parent', 'answers_for_survey', 'user_answer', 'date_start_answers')

    # def create(self, validated_data):
    #     answer = AnswersForSurvey.objects.update_or_create(
    #         surwey_parent=validated_data.get('surwey_parent', None),
    #         user_answer=validated_data.get('user_answer', None),
    #         answers_for_survey=validated_data.get('answers_for_survey', None)
    #     )
    #     return answer



class AddUserSerializer(serializers.ModelSerializer):
    '''Добавление пользователя'''
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create(
            ip=validated_data.get('ip', None),
            user_name=validated_data.get('user_name', None)
        )
        return user

