from django.contrib import admin
from .models import Question, Survey, User, Answer

admin.site.register(Survey)
admin.site.register(User)
admin.site.register(Question)
admin.site.register(Answer)

