"""
Serializers for accounts
"""
from django.contrib.auth import authenticate
from rest_framework.serializers import ModelSerializer, CharField, Serializer, ValidationError

from .models import CustomUser


class RegistrationSerializer(ModelSerializer):
    """
    class RegistrationSerializer for CustomUser
    """
    password = CharField(max_length=64, min_length=6, write_only=True)
    token = CharField(max_length=255, read_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'token', 'organization']

    def create(self, validated_data):
        """
        Create new user
        """
        return CustomUser.objects.create_user(**validated_data)


class LoginSerializer(Serializer):
    """
    class LoginSerializer
    """
    email = CharField(max_length=255)
    password = CharField(max_length=64, write_only=True)
    token = CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise ValidationError('An email address is required to log in.')
        if password is None:
            raise ValidationError('A password is required to log in.')

        user = authenticate(username=email, password=password)

        if user is None:
            raise ValidationError('A user with this email and password was not found.')

        if not user.is_active:
            raise ValidationError('This user has been deactivated.')

        return {
            'email': user.email,
            'token': user.token,
        }


class UserSerializer(ModelSerializer):
    """
    class UserSerializer
    """
    password = CharField(max_length=64, min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password', 'token',)
        read_only_fields = ('token', )

    def update(self, instance, validated_data):
        """
        update user
        """
        password = validated_data.pop('password', None)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()

        return instance
