from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Character 
from .serializers import CharacterReadSerializer

class CharacterListAPIView(ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterReadSerializer 

class CharacterDetailAPIView(RetrieveAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterReadSerializer
    lookup_field = 'id'
