from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели User."""

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role'
        )
        # read_only_fields = ('role',)

    def validate_name_me(self, data):
        if data.get('username') == 'me':
            raise serializers.ValidationError(
                'Использовать имя \'me\' запрещено.'
            )


class UserSignupSerializer(serializers.Serializer):
    """Сериализатор добавления пользователя и отправки кода."""

    username = serializers.RegexField(
        regex=r'^[\w.@+-]+\Z',
        error_messages={
            'invalid': ('Имя пользователя содержит недопустимый символ.')
        },
        max_length=150,
        required=True
    )
    email = serializers.EmailField(required=True, max_length=254)

    def validate_username(self, value):
        """
        Валидация 'me'.
        """
        if value == 'me':
            raise serializers.ValidationError(
                "Имя \'me\' зарезервировано системой.")
        return value

    def validate(self, attrs):
        username = attrs['username']
        email = attrs['email']
        if User.objects.filter(username=username, email=email).exists():
            return attrs
        elif User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                "Пользователь с таким именем сушествует")
        elif User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                "Пользователь с таким email сушествует")
        else:
            return attrs


class UserConfirmationCodeSerializer(serializers.Serializer):
    """Сериализатор подтверждения кода для получения токена."""
    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)