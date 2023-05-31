"""
Serializers for events
"""
from rest_framework.serializers import ModelSerializer

from .models import Event


class EventSerializer(ModelSerializer):
    """
    class EventSerializer
    """
    class Meta:
        model = Event
        fields = '__all__'
