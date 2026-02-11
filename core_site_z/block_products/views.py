from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from .models import Products, TestDrive, Profile
from .serializers import ProductSerializers, TestDriveSerializer


class ListProductPreview(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        queryset = Products.objects.all()
        serializer = ProductSerializers(queryset, many=True, context={'request': request})
        return Response(serializer.data)


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializers
    queryset = Products.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_context(self):
        return {'request': self.request}


class TestDriveViewSet(ModelViewSet):
    serializer_class = TestDriveSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return TestDrive.objects.filter(product_id=self.kwargs['product_pk'])

    def perform_create(self, serializer):
        serializer.save(
            product_id=self.kwargs['product_pk']
        )


class TelegramAuthView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        telegram_id = request.data.get('telegram_id')
        username = request.data.get('username', f'tg_{telegram_id}')

        profile = Profile.objects.filter(telegram_id=telegram_id).first()

        if profile:
            user = profile.user
        else:
            user = User.objects.create(username=username)
            Profile.objects.create(user=user, telegram_id=telegram_id)

        # Генерируем JWT-токены для пользователя
        refresh = RefreshToken.for_user(user)

        # Отдаём токены боту
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        })

