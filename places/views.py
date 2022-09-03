from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Place
from .serializers import PlaceReadSerializer

class PlaceListAPIView(ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceReadSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'category']
    ordering_fields = ['name', 'category']
    filterset_fields = ['name', 'category']

class PlaceDetailAPIView(RetrieveAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceReadSerializer
    lookup_field = 'id'
