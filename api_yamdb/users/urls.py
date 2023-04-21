from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    APIUserMe, UserViewSet, check_code_get_token, signup_send_code)

app_name = 'users'

router_v1 = DefaultRouter()
router_v1.register(r'v1/users', UserViewSet, basename='user')

auth_urlpatterns = [
    path('signup/', signup_send_code, name='signup'),
    path('token/', check_code_get_token, name='token'),
]

urlpatterns = [
    path('v1/auth/', include(auth_urlpatterns), name='auth'),
    path('v1/users/me/', APIUserMe.as_view(), name='me'),
    path('', include(router_v1 .urls), name='api-root'),
]
