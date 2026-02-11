from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import News
from .serializers import NewsSerializer


class NewsList(APIView):
    def get(self, request):
        queryset = News.objects.filter(is_active=True)[:3]
        serializer = NewsSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)


class NewsDetail(APIView):
    def get(self, request, slug):
        queryset = News.objects.filter(slug_news=slug, is_active=True).first()
        serializer = NewsSerializer(queryset, context={'request': request})
        return Response(serializer.data)

