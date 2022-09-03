from django.db import models
from rest_framework.reverse import reverse

from movies.models import Movie

class Chapter(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    movie_chapter = models.IntegerField()

    def get_absolute_url(self, request):
        return reverse('chapter-detail', kwargs={'id': self.id}, request=request)
    
    class Meta:
        db_table = 'chapters'
    
    def __str__(self):
        return str({
            'id': self.id,
            'name': self.name,
            'movie': self.movie,
            'movie_chapter': self.movie_chapter,
        })
    