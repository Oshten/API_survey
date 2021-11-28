from django.db import models

class User(models.Model):
    '''Пользователь'''

    ip = models.CharField('IP адреc', max_length=15)
    user_name = models.CharField('Имя пользователя', max_length=30, default=' ', blank=True)


    def __str__(self):
        return str(self.id)+ '. ' + self.user_name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Survey(models.Model):

    '''Опрос'''

    survey_name = models.CharField('Название', max_length=30)
    date_start = models.DateField('Дата старта', auto_now_add=True)
    date_finish = models.DateField('Дата окончания', auto_now=True)
    description = models.TextField('Описание')

    def __str__(self):
        return self.survey_name

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

# class QuestionWithAnswerText(models.Model):
#     '''Вопрос с ответом в виде текса'''
#
#     question = models.TextField('Вопрос')
#
#     def __str__(self):
#         return self.question
#
# class QuestionWithAnswerOption(models.Model):
#     '''Вопрос с выбором варианта ответа'''
#
#     question = models.TextField('Вопрос')
#     option_1 = models.TextField('Вариант 1')
#     option_2 = models.TextField('Вариант 2')
#     option_3 = models.TextField('Вариант 3')
#
#     def __str__(self):
#         return self.question
#
# class QuestionWithAnswerSomeOptions(models.Model):
#     '''Вопрос с выбором нескольких вариантов ответа'''
#
#     question = models.TextField('Вопрос')
#     option_1 = models.TextField('Вариант 1')
#     option_2 = models.TextField('Вариант 2')
#     option_3 = models.TextField('Вариант 3')
#
#     def __str__(self):
#         return self.question


class Question(models.Model):
    '''Вопрос опроса'''

    # CHOSE_TYPE_QUESTION = [
    #     (QuestionWithAnswerText, 'answer_text'),
    #     (QuestionWithAnswerOption, 'answer_option'),
    #     (QuestionWithAnswerSomeOptions, 'answer_some_options')
    # ]

    text_question = models.TextField('Текст вопроса')
    attachment = models.ForeignKey(
        Survey,
        verbose_name='Опрос',
        on_delete=models.CASCADE,
        related_name='questions'
    )

    def __str__(self):
        return self.text_question

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'




class Result(models.Model):
    '''Ответы на опрос'''

    user_result = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='user_result'
    )
    surwey_parent = models.ForeignKey(
        Survey,
        verbose_name='Опрос',
        on_delete=models.CASCADE,
        related_name='surwey_parent'
    )
    date_start_result = models.DateTimeField('Время начала ответов на опрос', auto_now_add=True)


    def __str__(self):
        return self.surwey_parent.survey_name

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'



class Answer(models.Model):
    '''Ответ на вопрос'''
    text_answer = models.TextField('Ответ')
    question_for_answer = models.ForeignKey(
        Question,
        verbose_name='Вопрос',
        on_delete=models.CASCADE,
        related_name='question_for_answer'
    )
    answers_for_survey = models.ForeignKey(
            Result,
            verbose_name='Результат',
            on_delete=models.CASCADE,
            related_name='answers_for_survey'
        )

    def __str__(self):
        return self.text_answer

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'








