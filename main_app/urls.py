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
    path('pokemon/<int:pokemon_id>/add_stats/', views.add_stats, name='add_stats'),
    path('pokemon/<int:pokemon_id>/assoc_item/<int:item_id>/', views.assoc_item, name='assoc_item'),
    path('pokemon/<int:pokemon_id>/unassoc_item.<int:item_id>/', views.unassoc_item, name='unassoc_item'),
    path('pokemon/<int:pokemon_id>/add_photo/', views.add_photo, name='add_photo'),
    path('item/', views.ItemList.as_view(), name='item_index'),
    path('item/<int:pk>/', views.ItemDetail.as_view(), name='item_detail'),
    path('item/create/', views.ItemCreate.as_view(), name='item_create'),
    path('item/<int:pk>/update/', views.ItemUpdate.as_view(), name='item_update'),
    path('item/<int:pk>/delete/', views.ItemDelete.as_view(), name='item_delete'),
]