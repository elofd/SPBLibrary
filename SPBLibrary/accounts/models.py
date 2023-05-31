"""
Model for CustomUser
"""
from datetime import datetime, timedelta

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
import jwt

from .manager import CustomUserManager
from organizations.models import Organization


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    class CustomUser
    """
    class Meta:
        verbose_name = 'user'

    email = models.EmailField(_('email address'), max_length=255, unique=True, db_index=True)
    USERNAME_FIELD = 'email'
    organization = models.ForeignKey(Organization, related_name='order_items', on_delete=models.PROTECT)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    @property
    def token(self):
        """
        Get user token
        """
        return self._generate_jwt_token()

    def get_full_name(self):
        """
        full name of user for django
        """
        return self.email

    def get_short_name(self):
        """
        short name of user for django
        """
        return self.email

    def _generate_jwt_token(self):
        """
        generate jwt token
        """
        dt = datetime.now() + timedelta(days=1)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token
