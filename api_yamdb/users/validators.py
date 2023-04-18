from django.contrib.auth.validators import UnicodeUsernameValidator


class YamdbUsernameValidator(UnicodeUsernameValidator):
    """Username валидатор по ТЗ"""
    regex = r'^[\w.@+-]+\Z'
    message = ('Имя пользователя содержит недопустимый символ')
