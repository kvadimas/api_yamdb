from django.db import models


class Genre(models.Model):
    name = models.CharField(
        'Название',
        max_length=256
    )
    slug = models.SlugField(
        max_length=50,
        unique=True
    )
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        'Название',
        max_length=256
    )
    slug = models.SlugField(
        max_length=50,
        unique=True
    )
    def __str__(self):
        return self.name


class Title(models.Model):
    """Произведения, к которым пишут отзывы (фильм, книга или песенка)."""
    name = models.CharField(
        'Название',
        max_length=256
    )
    year = models.IntegerField('Год выпуска')
    description = models.TextField('Описание')
    genre = models.ManyToManyField(
        Genre,
        through='GenreTitle',
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


class GenreTitle(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.genre} {self.title}'
