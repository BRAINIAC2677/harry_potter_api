from django.urls import path 

from .views import MovieListAPIView, MovieDetailAPIView

urlpatterns = [
    path('', MovieListAPIView.as_view(), name='movie-list'),
    path('<int:id>/', MovieDetailAPIView.as_view(), name='movie-detail'),  
]