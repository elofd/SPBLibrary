"""
URLS for events
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import EventViewSet

app_name = 'events'

routers = DefaultRouter()
routers.register('', EventViewSet)

urlpatterns = [
    path('api/', include(routers.urls))
]
