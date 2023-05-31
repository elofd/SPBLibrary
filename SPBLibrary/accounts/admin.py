"""
Admin for accounts app
"""
from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class AccountsAdmin(admin.ModelAdmin):
    """
    class AccountsAdmin
    """
    list_display = 'pk', 'email', 'organization', 'is_staff', 'is_superuser', 'is_active',
    list_filter = 'organization',
    search_fields = 'email', 'organization__title'


