from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from rest_framework import filters, permissions, status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken

from .models import User
from .serializers import (
    UserConfirmationCodeSerializer, UserSerializer, UserSignupSerializer)
from api.permissions import IsAdminSuperuser


class UserViewSet(viewsets.ModelViewSet):
    """Вьсет модели USER"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminSuperuser,)
    filter_backends = (filters.SearchFilter,)
    filter_fields = ('username',)
    search_fields = ('username',)
    lookup_field = 'username'
    pagination_class = PageNumberPagination
    http_method_names = ['get', 'post', 'patch', 'delete']


class APIUserMe(APIView):
    """Вбюсет для ендпойнта /me"""

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        if request.user.is_authenticated:
            user = get_object_or_404(User, pk=request.user.pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        return Response({'error': 'Необходимо авторизоваться'},
                        status=status.HTTP_401_UNAUTHORIZED)

    def patch(self, request):
        if request.user.is_authenticated:
            user = get_object_or_404(User, pk=request.user.pk)
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.validated_data['role'] = user.role
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(
            'Дествие недоступно для неавторизованного',
            status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def signup_send_code(request):
    """Ригистрация и отправка кода подтверждения"""

    serializer = UserSignupSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.initial_data['username']
    serializer.save()
    user = get_object_or_404(User, username=username)
    confirmation_code = default_token_generator.make_token(user)

    context = {
        'title': 'Код подтверждения Yamdb',
        'username': user.username,
        'confirmation_code': confirmation_code
    }
    message = get_template('email_confirm.html').render(context)
    send_mail(
        subject='Код подтверждения Yamdb',
        message=message,
        from_email='admin@yamdb.fake',
        recipient_list=[user.email]
    )
    return Response(serializer.initial_data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def check_code_get_token(request):
    """Проверка кода и выдача токена"""

    serializer = UserConfirmationCodeSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.data.get('username')
        confirmation_code = serializer.data.get('confirmation_code')
        user = get_object_or_404(User, username=username)
        if not default_token_generator.check_token(user, confirmation_code):
            msg = {'confirmation_code': 'Код подтверждения невалиден'}
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)
        msg = {'token': str(AccessToken.for_user(user))}    # генерация токена
        return Response(msg, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
