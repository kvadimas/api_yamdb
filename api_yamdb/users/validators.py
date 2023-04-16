from django.contrib.auth.validators import UnicodeUsernameValidator


class YamdbUsernameValidator(UnicodeUsernameValidator):
    regex = r'^[\w.@+-]+\Z'
    message = ('Имя пользователя содержит недопустимый символ')
