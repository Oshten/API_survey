from django.contrib import admin
from .models import Question, Survey, User

admin.site.register(Survey)
admin.site.register(User)
admin.site.register(Question)
admin.site.register(Question.QuestionWithAnswerText)
admin.site.register(Question.QuestionWithAnswerOption)
admin.site.register(Question.QuestionWithAnswerSomeOptions)
