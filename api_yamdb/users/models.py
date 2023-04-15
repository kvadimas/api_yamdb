from django.contrib.auth.models import AbstractUser
from django.db import models

from .validators import YamdbUsernameValidator


USER_ROLES = (
    ('user', 'user'),
    ('moderator', 'moderator'),
    ('admin', 'admin'),
)


class User(AbstractUser):
    username = models.CharField(
        verbose_name='Имя пользователя',
        max_length=150,
        validators=(YamdbUsernameValidator,),
        unique=True,
        blank=False,
    )
    email = models.EmailField(
        verbose_name='Email',
        max_length=254,
        blank=False,
        unique=True,
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=150,
        blank=True,
    )

    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=150,
        blank=True,
    )

    bio = models.TextField(
        verbose_name='О себе',
    )

    role = models.CharField(
        verbose_name='Роль',
        max_length=15,
        choices=USER_ROLES,
        default='user',
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id',)

    def __str__(self):
        return self.username

    @property
    def is_user(self):
        return self.role == 'user'

    @property
    def is_moderator(self):
        return self.role == 'moderator'

    @property
    def is_admin(self):
        return self.role == 'admin'
