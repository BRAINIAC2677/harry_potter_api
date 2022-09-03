from django.urls import path

from .views import DialogueListAPIView, DialogueDetailAPIView

urlpatterns = [
    path('', DialogueListAPIView.as_view(), name='dialogue-list'),
    path('<int:id>/', DialogueDetailAPIView.as_view(), name='dialogue-detail'),
]
