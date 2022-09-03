from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Spell
from .serializers import SpellReadSerializer

class SpellListAPIView(ListAPIView):
    queryset = Spell.objects.all()
    serializer_class = SpellReadSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'incantation', 'effect', 'light']
    ordering_fields = ['name', 'incantation', 'effect', 'light']
    filterset_fields = ['name', 'incantation', 'effect', 'light']

class SpellDetailAPIView(RetrieveAPIView):
    queryset = Spell.objects.all()
    serializer_class = SpellReadSerializer
    lookup_field = 'id'