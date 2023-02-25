from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Gotta catch 'em all!</h1>")

def about(request):
    return render(request, 'about.html')

def pokemon_index(request):
    return render(request, 'pokemon/index.html', {'pokemon': pokemon})

class Pokemon:
    def __init__(self, name, type, level, stage):
        self.name = name
        self.type = type
        self.level = level
        self.stage = stage

pokemon = [
    Pokemon('Bulbasaur', 'Grass/Poison', 5, 1),
    Pokemon('Squirtle', 'Water', 5, 1),
    Pokemon('Charmander', 'Fire', 5, 1),
    Pokemon('Pikachu', 'Electric', 81, 2)
]
