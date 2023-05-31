"""
View for events
"""
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated

from .models import Event
from .serializers import EventSerializer


class EventViewSet(ModelViewSet):
    """
    class EventViewSet (full CRUD)
    """
    queryset = Event.objects.all().prefetch_related('organizations')
    serializer_class = EventSerializer
    permission_classes = IsAuthenticated,
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['date']
