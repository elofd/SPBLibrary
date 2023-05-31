"""
Admin for events
"""
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Event


@admin.register(Event)
class EventsAdmin(admin.ModelAdmin):
    """
    class EventsAdmin
    """
    list_display = 'pk', 'title', 'date',
    list_filter = 'date',
    search_fields = 'title',
    readonly_fields = 'preview',

    def preview(self, obj):
        """
        Add preview image field
        """
        return mark_safe(f'<img src="{obj.image.url}">')
