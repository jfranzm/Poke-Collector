from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pokemon

from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def pokemon_index(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'pokemon/index.html', {'pokemons': pokemons})

def pokemon_detail(request, pokemon_id):
  pokemon = Pokemon.objects.get(id=pokemon_id)
  return render(request, 'pokemon/detail.html', { 'pokemon': pokemon })

class PokeCreate(CreateView):
    model = Pokemon
    fields = '__all__'
    success_url = '/pokemon/'

class PokeUpdate(UpdateView):
    model = Pokemon
    fields = ['type', 'level', 'stage']

class PokeDelete(DeleteView):
    model = Pokemon
    success_url = '/pokemon/'