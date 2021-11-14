from django.shortcuts import render
from rest_framework import viewsets

from .models import Survey, Question, User
from .serializers import SurveySerializer, QuestionSerializer, UserSerializer

class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all().order_by('name')
    serializer_class = SurveySerializer


