from rest_framework.generics import ListAPIView, RetrieveAPIView

from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Movie 
from .serializers import MovieReadSerializer

class MovieListAPIView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieReadSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['title', 'release_year', 'runtime', 'budget', 'box_office_revenue']
    ordering_fields = ['title','release_year', 'runtime', 'budget', 'box_office_revenue']
    filterset_fields = ['title','release_year', 'runtime', 'budget', 'box_office_revenue']

class MovieDetailAPIView(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieReadSerializer
    lookup_field = 'id'
