from django.urls import path 

from .views import SpellListAPIView, SpellDetailAPIView

urlpatterns = [
    path('', SpellListAPIView.as_view(), name='spell-list'),
    path('<int:id>/', SpellDetailAPIView.as_view(), name='spell-detail'),
]