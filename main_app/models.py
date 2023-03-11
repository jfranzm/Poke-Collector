from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

STATS = (
    ('HP', 'HP'),
    ('ATK', 'Attack'),
    ('DEF', 'Defense'),
    ('SP. ATK', 'Sp. Atk'),
    ('SP. DEF', 'Sp. Def'),
    ('SPD', 'Speed')
)
class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    effects = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
            return reverse('item_detail', kwargs={'pk': self.id})
    
class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    level = models.IntegerField()
    stage = models.IntegerField()
    item = models.ManyToManyField(Item)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('pokemon_detail', kwargs={'pokemon_id': self.id})

class Stats(models.Model):
    Stat = models.CharField(
        max_length=7,
            choices=STATS,
            default=STATS[0][0]
    )
    Stat_Value = models.IntegerField(
        default=1
    )
    EVs = models.IntegerField(
       default=1,
       validators= [
        MaxValueValidator(252),
        MinValueValidator(0)
       ]
    )
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_Stat_display()}"
    
    class Meta:
        ordering = ['Stat']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for pokemon_id: {self.pokemon_id} @{self.url}"
    
