from rest_framework.reverse import reverse
from django.db import models

# Create your models here.
class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    release_year = models.IntegerField()
    runtime = models.IntegerField()
    budget = models.IntegerField()
    box_office_revenue = models.IntegerField()

    def get_absolute_url(self, request):
        return reverse('movie-detail', args=[str(self.id)], request=request)

    class Meta:
        db_table = 'movies'
    
    def __str__(self):
        return str({
            'id': self.id,
            'title': self.title,
            'release_year': self.release_year,
            'runtime': self.runtime,
            'budget': self.budget,
            'box_office_revenue': self.box_office_revenue
        })