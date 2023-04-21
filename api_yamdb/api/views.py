from django.shortcuts import get_object_or_404
from django.db.models import Avg
from rest_framework import viewsets, mixins
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from reviews.models import Category, Genre, Title

from api.permissions import (IsAdminSuperuserOrReadOnly,
                          IsAuthorAdminModeratorOrReadOnly)
from api.serializers import (CategorySerializer, GenreSerializer,
                             TitleSerializer, ReviewSerializer,
                             CommentSerializer, TitleCreateSerializer)
from reviews.models import Review
from api.filters import TitleFilter


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all().annotate(
        rating=Avg('reviews__score')).all()
    # serializer_class = TitleSerializer
    permission_classes = (IsAdminSuperuserOrReadOnly,)
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = TitleFilter
    #filter_backends = (SearchFilter,)
    #search_fields = (
    #    'category__slug',
    #    'genre__slug',
    #    'name',
    #    'year'
    #)

    def get_serializer_class(self):
        if self.request.method in ('POST', 'PATCH',):
            return TitleCreateSerializer
        return TitleSerializer


class CategoryViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminSuperuserOrReadOnly,)
    pagination_class = LimitOffsetPagination
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
    lookup_field = ('slug')


class GenreViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminSuperuserOrReadOnly,)
    pagination_class = LimitOffsetPagination
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
    lookup_field = ('slug')


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthorAdminModeratorOrReadOnly,)

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
    permission_classes = (IsAuthorAdminModeratorOrReadOnly,)

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
