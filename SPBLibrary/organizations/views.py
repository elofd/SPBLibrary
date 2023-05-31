"""
View for organizations
"""
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Organization
from .serializers import OrganizationSerializer


class OrganizationsViewSet(ModelViewSet):
    """
    class OrganizationsListCreateView (full CRUD)
    """
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = IsAuthenticated,

