"""
Model for Event
"""
from django.db import models
from django.utils.translation import gettext_lazy as _

from organizations.models import Organization


class Event(models.Model):
    """
    class Event
    """
    title = models.CharField(_('title'), max_length=255, db_index=True)
    description = models.TextField(_('description'))
    organizations = models.ManyToManyField(Organization, related_name='events')
    image = models.ImageField(upload_to='events/')
    date = models.DateTimeField()

    def __str__(self):
        return self.title
