from django.urls import path

from .views import PlaceListAPIView, PlaceDetailAPIView

urlpatterns = [
    path('', PlaceListAPIView.as_view(), name='place-list'),
    path('<int:id>/', PlaceDetailAPIView.as_view(), name='place-detail'),
]
