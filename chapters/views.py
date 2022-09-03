from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Chapter
from .serializers import ChapterReadSerializer

class ChapterListAPIView(ListAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterReadSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'movie']
    ordering_fields = ['name', 'movie']
    filterset_fields = ['name', 'movie']

class ChapterDetailAPIView(RetrieveAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterReadSerializer
    lookup_field = 'id'