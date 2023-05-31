"""
Model for Organization
"""
from django.db import models
from django.utils.translation import gettext_lazy as _


class Organization(models.Model):
    """
    Class Organization
    """
    title = models.CharField(_('title'), max_length=255, unique=True, db_index=True)
    description = models.TextField(_('description'))
    address = models.CharField(_('address'), max_length=255, db_index=True)
    postcode = models.CharField(_('postcode'), max_length=10)

    def __str__(self):
        return self.title
