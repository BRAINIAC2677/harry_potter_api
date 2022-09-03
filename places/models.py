from django.db import models
from rest_framework.reverse import reverse

class Place(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    def get_absolute_url(self, request):
        return reverse('place-detail', kwargs={'id': self.id}, request=request)
    
    class Meta:
        db_table = 'places'
    
    def __str__(self):
        return str({
            'id': self.id,
            'name': self.name,
            'category': self.category,
        })