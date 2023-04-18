from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели User."""

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'bio',)

    def validate_name_me(self, data):
        if data.get('username') == 'me':
            raise serializers.ValidationError(
                'Использовать имя \'me\' запрещено.'
            )


class UserSignupSerializer(serializers.ModelSerializer):
    """Сериализатор для создания объекта класса User."""

    class Meta:
        model = User
        fields = (
            'username', 'email'
        )

    def validate(self, data):
        """Валидация username, email, me"""
        if User.objects.filter(username=data.get('username')):
            raise serializers.ValidationError(
                'Пользователь с таким username уже существует'
            )
        if User.objects.filter(email=data.get('email')):
            raise serializers.ValidationError(
                'Пользователь с таким email уже существует'
            )
        if data.get('username') == 'me':
            raise serializers.ValidationError(
                'Имя \'me\' зарезервировано системой'
            )

        return data


class UserConfirmationCodeSerializer(serializers.Serializer):
    """Сериализатор подтверждения кода для получения токена."""
    email = serializers.EmailField(required=True)
    confirmation_code = serializers.CharField(required=True)
