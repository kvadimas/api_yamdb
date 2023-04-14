from rest_framework import serializers
from reviews.models import Title, Genre, Category, GenreTitle
from datetime import datetime


class GenreSerializer(serializers.ModelSerializer):
    lookup_field = 'slug'

    class Meta:
        fields = ('name', 'slug')
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Genre.objects.all(),
        many=True
    )
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Category.objects.all()
    )

    class Meta:
        fields = ('name', 'year', 'description', 'genre', 'category')
        model = Title

    """ def create(self, validated_data):
        genres = validated_data.pop('genre')
        title = Title.objects.create(**validated_data)
        for genre in genres:
            current_genre, status = Genre.objects.get_or_create(
                **genre)
            GenreTitle.objects.create(
                genre=current_genre, title=title)
        return title"""

    def validate(self, data):
        if data['year'] > datetime.now().year:
            raise serializers.ValidationError(
                "Год выпуска не может быть больше текущего!"
            )
        return data


class CategorySerializer(serializers.ModelSerializer):
    lookup_field = 'slug'

    class Meta:
        fields = ('name', 'slug')
        model = Category
