from django.db import models


class Title(models.Model):
    """Произведения, к которым пишут отзывы (фильм, книга или песенка)."""
    name = models.CharField(
        'Название',
        max_length=256
    )
    year = models.IntegerField('Год выпуска')
    description = models.TextField('Описание')
    genre = models.ForeignKey(
        Genre,
        related_name='titles',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    category = models.ForeignKey(
        Category,
        related_name='titles',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        return self.name
