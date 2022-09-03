from rest_framework import serializers

from .models import Chapter

class ChapterReadSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    movie = serializers.SerializerMethodField()
    class Meta:
        model = Chapter
        fields = ['id','url', 'name', 'movie', 'movie_chapter']
    
    def get_url(self, obj):
        return obj.get_absolute_url(self.context['request'])
    
    def get_movie(self, obj):
        return obj.movie.id 
