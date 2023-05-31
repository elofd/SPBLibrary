"""
Admin for organizations app
"""
from django.contrib import admin

from .models import Organization


@admin.register(Organization)
class OrganizationsAdmin(admin.ModelAdmin):
    """
    class OrganizationsAdmin
    """
    list_display = "pk", 'title', 'address', 'postcode'
    search_fields = 'title', 'postcode'
