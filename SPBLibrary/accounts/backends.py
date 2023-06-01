"""
Backend for CustomUser JWT Tokens
"""
import jwt
from rest_framework import authentication, exceptions
from django.conf import settings

from .models import CustomUser


class JWTAuthentication(authentication.BaseAuthentication):
    """
    class JWTAuthentication
    """
    authentication_header_prefix = 'Token'

    def authenticate(self, request):
        """
        authenticate method
        """
        request.user = None
        auth_header = authentication.get_authorization_header(request).split()
        auth_header_prefix = self.authentication_header_prefix.lower()

        if not auth_header:
            return None

        if len(auth_header) != 2:
            return None

        prefix = auth_header[0].decode('utf-8')
        token = auth_header[1].decode('utf-8')

        if prefix.lower() != auth_header_prefix:
            return None

        return self._authenticate_credentials(request, token)

    def _authenticate_credentials(self, request, token):
        """
        try authenticate method
        """
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.exceptions.ExpiredSignatureError:
            msg = 'Authenticate Error. Old token. Login again'
            raise exceptions.AuthenticationFailed(msg)
        except Exception:
            msg = f'Authenticate Error. Cannot decode token'
            raise exceptions.AuthenticationFailed(msg)

        try:
            user = CustomUser.objects.get(pk=payload['id'])
        except CustomUser.DoesNotExist:
            msg = 'User not find.'
            raise exceptions.AuthenticationFailed(msg)

        if not user.is_active:
            msg = 'User deactivated.'
            raise exceptions.AuthenticationFailed(msg)

        return (user, token)
