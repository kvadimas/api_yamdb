from api.views import TitleViewSet, CategoryViewSet, GenreViewSet

from django.urls import include, path
from rest_framework.routers import DefaultRouter

app_name = 'api'

# Создаётся роутер
router_v1 = DefaultRouter()
router_v1.register('titles', TitleViewSet)
router_v1.register('category', CategoryViewSet)
router_v1.register('genre', GenreViewSet)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
