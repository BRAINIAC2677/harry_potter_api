from django.db import models
from rest_framework.reverse import reverse

class Spell(models.Model):
    id = models.IntegerField(primary_key=True)
    incantation = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    effect = models.TextField()
    light = models.CharField(max_length = 255, null=True)

    def get_absolute_url(self, request):
        return reverse('spell-detail', args=[str(self.id)], request=request)
    
    class Meta:
        db_table = 'spells'
    
    def __str__(self):
        return str({
            'id': self.id,
            'incantation': self.incantation,
            'name': self.name,
            'effect': self.effect,
            'light': self.light,
        })
    