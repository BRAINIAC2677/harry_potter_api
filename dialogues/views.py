from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Dialogue
from .serializers import DialogueReadSerializer

class DialogueListAPIView(ListAPIView):
    queryset = Dialogue.objects.all()
    serializer_class = DialogueReadSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['dialogue']
    ordering_fields = ['chapter','place','character', 'dialogue']
    filterset_fields = ['chapter', 'place', 'character']

class DialogueDetailAPIView(RetrieveAPIView):
    queryset = Dialogue.objects.all()
    serializer_class = DialogueReadSerializer
    lookup_field = 'id'