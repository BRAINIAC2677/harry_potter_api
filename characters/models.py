from django.db import models

# Create your models here.
class Character(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    species = models.CharField(max_length=60, null=True)
    gender = models.CharField(max_length=20, null=True)
    house = models.CharField(max_length=60, null=True)
    patronus = models.CharField(max_length=20, null=True)
    wand_wood = models.CharField(max_length=20, null=True)
    wand_core = models.CharField(max_length=60, null=True)

    class Meta:
        db_table = 'characters'
    
    def __str__(self):
        return str({
            'id': self.id,
            'name': self.name,
            'species': self.species,
            'gender':self.gender,
            'house':self.house,
            'patronus':self.patronus,
            'wand_wood':self.wand_wood,
            'wand_core':self.wand_core
        })
