from api.serializers import (CategorySerializer, GenreSerializer,
                             TitleSerializer)
from django.shortcuts import render
from reviews.models import Title, Category, Genre
from rest_framework import permissions, viewsets
from api.serializers import TitleSerializer, CategorySerializer, GenreSerializer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from reviews.models import Category, Genre, Title


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    #permission_classes = (permissions.IsAuthenticated,)
    pagination_class = LimitOffsetPagination
    filter_backends = (SearchFilter,)
    search_fields = (
        'category__slug',
        'genre__slug',
        'name',
        'year'
    )


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    #permission_classes = (permissions.IsAuthenticated,)
    pagination_class = LimitOffsetPagination
    filter_backends = (SearchFilter,)
    search_fields = ('name',)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    #permission_classes = (permissions.IsAuthenticated,)
    pagination_class = LimitOffsetPagination
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
