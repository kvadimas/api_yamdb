from api.views import TitleViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter

app_name = 'api'

# Создаётся роутер
router = DefaultRouter()
router.register('titles', TitleViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]