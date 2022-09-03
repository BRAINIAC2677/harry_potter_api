from django.urls import path 

from .views import ChapterListAPIView, ChapterDetailAPIView

urlpatterns =[
    path('', ChapterListAPIView.as_view(), name='chapter-list'),
    path('<int:id>/', ChapterDetailAPIView.as_view(), name='chapter-detail'),
]