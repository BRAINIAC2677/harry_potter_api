from django.db import models
from rest_framework.reverse import reverse

from chapters.models import Chapter
from places.models import Place
from characters.models import Character

class Dialogue(models.Model):
    id = models.IntegerField(primary_key=True)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    dialogue = models.TextField()

    def get_absolute_url(self, request):
        return reverse('dialogue-detail', kwargs={'id': self.id}, request=request)
    
    class Meta:
        db_table = 'dialogues'
    
    def __str__(self):
        return str({
            'id': self.id,
            'chapter': self.chapter,
            'place': self.place,
            'character': self.character,
            'dialogue': self.dialogue,
        })

