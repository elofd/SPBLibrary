"""
URLS for accounts
"""
from django.urls import path

from .views import RegistrationApiView, LoginApiView, UserRetrieveUpdateApiView

app_name = 'accounts'

urlpatterns = [
    path('registration/', RegistrationApiView.as_view(), name='registration'),
    path('login/', LoginApiView.as_view(), name='login'),
    path('user', UserRetrieveUpdateApiView.as_view(), name='user'),
]





