from django.contrib import admin
from .models import Question, Survey, User, Result, Answer

admin.site.register(Survey)
admin.site.register(User)
admin.site.register(Question)
admin.site.register(Result)
admin.site.register(Answer)

