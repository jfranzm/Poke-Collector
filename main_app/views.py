from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
import uuid
import boto3
from .models import Pokemon, Item, Photo
from .forms import StatForm

S3_BASE_URL = 'https://s3-accesspoint.ca-central-1.amazonaws.com'
BUCKET = 'pokecollector1'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def pokemon_index(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'pokemon/index.html', {'pokemons': pokemons})

def pokemon_detail(request, pokemon_id):
  pokemon = Pokemon.objects.get(id=pokemon_id)
  items_pokemon_doesnt_have = Item.objects.exclude(id__in = pokemon.item.all().values_list('id'))
  stat_form = StatForm()
  return render(request, 'pokemon/detail.html', { 'pokemon': pokemon, 'stat_form': stat_form, 'item': items_pokemon_doesnt_have })

def add_stats(request, pokemon_id):
    form = StatForm(request.POST)
    if form.is_valid():
        new_stat = form.save(commit=False)
        new_stat.pokemon_id = pokemon_id
        new_stat.save()
    return redirect('pokemon_detail', pokemon_id=pokemon_id)

def add_photo(request, pokemon_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = 'pokecollector1/' + uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            Photo.objects.create(url=url, pokemon_id=pokemon_id)
        except:
            print('An error occurred uploading file to S3')
    return redirect('pokemon_detail', pokemon_id=pokemon_id)

def assoc_item(request, pokemon_id, item_id):
    Pokemon.objects.get(id=pokemon_id).item.add(item_id)
    return redirect('pokemon_detail', pokemon_id=pokemon_id)

def unassoc_item(reqest, pokemon_id, item_id):
    Pokemon.objects.get(id=pokemon_id).item.remove(item_id)
    return redirect('pokemon_detail', pokemon_id=pokemon_id)

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

class ItemList(ListView):
    model = Item

class ItemDetail(DetailView):
    model = Item

class ItemCreate(CreateView):
    model = Item
    fields = '__all__'

class ItemUpdate(UpdateView):
    model = Item
    fields = ['name', 'description', 'effects']

class ItemDelete(DeleteView):
    model = Item
    success_url = '/items/'