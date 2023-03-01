from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pokemon/', views.pokemon_index, name='pokemon_index'),
    path('pokemon/<int:pokemon_id>/', views.pokemon_detail, name='pokemon_detail'),
    path('pokemon/create/', views.PokeCreate.as_view(), name='pokemon_create'),
    path('pokemon/<int:pk>/update', views.PokeUpdate.as_view(), name='pokemon_update'),
    path('pokemon/<int:pk>/delete', views.PokeDelete.as_view(), name='pokemon_delete'),
]