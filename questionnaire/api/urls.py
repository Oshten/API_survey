from django.urls import path, include
from rest_framework import routers
from .views import SurveyViewSet

router = routers.DefaultRouter()
router.register(r'survey', SurveyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]