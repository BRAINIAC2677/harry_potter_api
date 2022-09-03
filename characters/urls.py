from django.urls import path 

from .views import CharacterListAPIView, CharacterDetailAPIView

urlpatterns = [
    path('', CharacterListAPIView.as_view(), name='character-list'),
    path('<int:id>/', CharacterDetailAPIView.as_view(), name='character-detail')
]