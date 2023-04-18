from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from users.models import User


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


class CommentReviewBase(models.Model):
    text = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='%(class)ss')
    pub_date = models.DateTimeField(
        auto_now_add=True, db_index=True)

    class Meta:
        abstract = True
        ordering = ('-pub_date',)

    def __str__(self):
        return self.text[:80]


class Review(CommentReviewBase):
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='reviews')
    score = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )

    class Meta(CommentReviewBase.Meta):
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author'],
                name='unique_title_author'
            )
        ]


class Comment(CommentReviewBase):
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments')

    class Meta(CommentReviewBase.Meta):
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
