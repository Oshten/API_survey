from rest_framework import serializers
from .models import Question, Survey, User, Result, Answer


class UserSerializer(serializers.ModelSerializer):
    '''Вывод пользователя'''

    class Meta:
        model = User
        fields = ('id', 'ip', 'user_name',)

class QuestionSerializer(serializers.ModelSerializer):
    '''Вывод вопросов'''

    class Meta:
        model = Question
        fields = ('id', 'text_question', 'attachment')

# class QuestionListSerializer(serializers.ModelSerializer):
#     '''Вывод вопросов одного опроса'''
#
#     class Meta:
#         model = Question
#         fields = ('__all__')




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


class CreateResultSerializer(serializers.ModelSerializer):
    '''Добавление ответов на опрос'''

    class Meta:
        model = Result
        fields = ('surwey_parent', 'user_result', 'date_start_result')


# class ResultListSerializer(serializers.ModelSerializer):
#     '''Добавление ответов на опрос'''
#     surwey_parent = SurveySerializer(read_only=True)
#     user_result = UserSerializer(read_only=True)
#
#     class Meta:
#         model = Result
#         fields = ('surwey_parent', 'user_result', 'date_start_result')
#
#     def create(self, validated_data):
#         result = Result.objects.update_or_create(
#             question_for_answer=validated_data.get('surwey_parent', None),
#             answers_for_survey=validated_data.get('user_result', None),
#         )
#         return result


class AnswersListSerializer(serializers.ModelSerializer):
    '''Вывод ответов на вопросы'''

    class Meta:
        model = Answer
        fields = ('id', 'text_answer')


# class CreateAnswerSerializer(serializers.ModelSerializer):
#     '''Добавление и вывод ответов на вопросы'''
#
#     class Meta:
#         model = Answer
#         fields = ('__all__')


class AnswerDetalsSerializer(serializers.ModelSerializer):
    '''Вывод деталей ответа, корректировка и удаление ответа'''
    question_for_answer = QuestionSerializer(read_only=True)
    answers_for_survey = CreateResultSerializer(read_only=True)

    class Meta:
        model = Answer
        fields = ('__all__')


class ResultDetalsSerializer(serializers.ModelSerializer):
    '''Вывод деталей ответов на опросы'''
    surwey_parent = SurveyDetalsSerializer(read_only=True)
    user_result = UserSerializer(read_only=True)

    answers_for_survey = AnswersListSerializer(many=True)

    class Meta:
        model = Result
        fields = ('user_result', 'surwey_parent', 'date_start_result', 'answers_for_survey')




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



class AllResaltsSerializer(serializers.ModelSerializer):
    '''Вывод результатов обного пользователя'''
    answers_for_survey = AnswerDetalsSerializer(read_only=True, many=True)
    surwey_parent = SurveySerializer(read_only=True)

    class Meta:
        model = Result
        fields = ('id', 'surwey_parent', 'date_start_result', 'answers_for_survey')


class AllUsersAndResultsSerializer(serializers.ModelSerializer):
    '''Вывод всех пользователей и их ответы'''
    user_result = AllResaltsSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ('id', 'ip', 'user_name', 'user_result')

