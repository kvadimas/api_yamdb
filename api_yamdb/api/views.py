from django.shortcuts import render
from api.models import Title, Genre
from rest_framework import permissions, viewsets
from api.serializers import TitleSerializer, GenreSerializer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import SearchFilter


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = (SearchFilter,)
    search_fields = (
        'category__slug',
        'genre__slug',
        'name',
        'year'
    )


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
