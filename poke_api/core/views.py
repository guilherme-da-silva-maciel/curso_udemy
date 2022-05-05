from django import http
from django.http import Http404
from django.shortcuts import render,get_list_or_404,get_object_or_404
from .utils.pokemons.factory import make_pokemons
from .models import Pokedex, Tipo

def home(request):
    pokemons = Pokedex.objects.filter(is_published=True)
    return render(request,'pokemons/pages/home.html',context={
        'pokemons' : pokemons
    })

def tipo(request,tipo_id):
    pokemons = get_list_or_404(Pokedex.objects.filter(tipo__id=tipo_id,is_published=True).order_by('-id'))

    return render(request,'pokemons/pages/home.html',context={
        'pokemons' : pokemons,
        'type' : f'{pokemons[0].tipo.tipo}'
    })

def poke(request,id):
    pokemon_description = Pokedex.objects.filter(id=id,is_published=True).order_by('-id').first()
    return render(request,'pokemons/pages/poke-view.html',context={
        'pokemon' : pokemon_description,
        'is_detail_page' : True
    })

def search(request):
    search_term = request.GET.get()

    if not search_term:
        raise Http404()

    pokemon = Pokedex.objects.filter(
        name__icontains=search_term
    )

    return render(request,'pokemons/partials/search_pok.html',{
        'page_title' : f'Search for {search_term}',
        'search_term' : search_term,
        'name' : pokemon
    })
    

# Create your views here.
