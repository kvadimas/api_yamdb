from datetime import datetime

from rest_framework import serializers

from reviews.models import Category, Comment, Genre, Review, Title


class GenreSerializer(serializers.ModelSerializer):
    lookup_field = 'slug'

    class Meta:
        fields = ('name', 'slug')
        model = Genre


class CategorySerializer(serializers.ModelSerializer):
    lookup_field = 'slug'

    class Meta:
        fields = ('name', 'slug')
        model = Category


class TitleSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(required=False)
    genre = GenreSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        fields = (
            'id', 'rating', 'name', 'year', 'description', 'genre', 'category')
        model = Title


class TitleCreateSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Genre.objects.all(),
        many=True)
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Category.objects.all())

    class Meta:
        model = Title
        fields = (
            'id', 'name', 'year', 'description', 'genre', 'category')

    def validate_year(self, value):
        if isinstance(value, int) and value > datetime.now().year:
            raise serializers.ValidationError(
                "Год выпуска не может быть больше текущего!"
            )
        return value


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Review
        fields = ('id', 'text', 'author', 'score', 'pub_date')

    def validate(self, data):
        title = self.context.get('view').kwargs.get('title_id')
        author = self.context.get('request').user
        if (
            self.context.get('request').method == 'POST'
            and Review.objects.filter(author=author, title=title).exists()
        ):
            raise serializers.ValidationError(
                'Вы уже оставляли отзыв на это произведение!'
            )
        return data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date')
