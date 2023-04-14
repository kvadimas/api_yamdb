from api.views import TitleViewSet, CategoryViewSet, GenreViewSet

from django.urls import include, path
from rest_framework.routers import DefaultRouter

app_name = 'api'

# Создаётся роутер
router = DefaultRouter()
router.register('titles', TitleViewSet)
router.register('category', CategoryViewSet)
router.register('genre', GenreViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]