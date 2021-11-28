from django.contrib import admin
from django.urls import path, include
# from . import yasg

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls'))
]

# urlpatterns =+ yasg.urlpatterns
