from rest_framework.generics import ListAPIView, RetrieveAPIView

from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Character 
from .serializers import CharacterReadSerializer

class CharacterListAPIView(ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterReadSerializer 
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name', 'species', 'gender', 'house', 'patronus', 'wand_wood', 'wand_core']
    search_fields = ['name', 'species', 'gender', 'house', 'patronus', 'wand_wood', 'wand_core']
    ordering_fields = ['name', 'species', 'gender', 'house', 'patronus', 'wand_wood', 'wand_core']

class CharacterDetailAPIView(RetrieveAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterReadSerializer
    lookup_field = 'id'
