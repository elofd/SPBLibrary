"""
URLS for organizations
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import OrganizationsViewSet


app_name = 'organizations'

routers = DefaultRouter()
routers.register('', OrganizationsViewSet)

urlpatterns = [
    path('api/', include(routers.urls))
]
