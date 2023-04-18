from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Avg
from rest_framework import permissions, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from reviews.models import Category, Genre, Title
from .permissions import IsAuthorOrModeratorOrReadOnly
from api.serializers import (CategorySerializer, GenreSerializer,
                             TitleSerializer, ReviewSerializer,
                             CommentSerializer)
from reviews.models import Review


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all().annotate(
        rating=Avg('reviews__score')).all()
    serializer_class = TitleSerializer
    # permission_classes = (permissions.IsAuthenticated,)
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
    # permission_classes = (permissions.IsAuthenticated,)
    pagination_class = LimitOffsetPagination
    filter_backends = (SearchFilter,)
    search_fields = ('name',)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    pagination_class = LimitOffsetPagination
    filter_backends = (SearchFilter,)
    search_fields = ('name',)


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthorOrModeratorOrReadOnly,
                          IsAuthenticatedOrReadOnly,)

    @property
    def title(self):
        return get_object_or_404(Title, pk=self.kwargs.get('title_id'))

    def get_queryset(self):
        return self.title.reviews.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, title=self.title)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthorOrModeratorOrReadOnly,
                          IsAuthenticatedOrReadOnly,)

    @property
    def review(self):
        return get_object_or_404(Review, pk=self.kwargs.get('review_id'))

    def get_queryset(self):
        return self.review.comments.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            review=self.review
        )
