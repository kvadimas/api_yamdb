from rest_framework import serializers
from api.models import Title, Genre, Category
from datetime import datetime


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

    def validate(self, data):
        if data['year'] > datetime.now().year:
            raise serializers.ValidationError(
                "Год выпуска не может быть больше текущего!"
            )
        return data
