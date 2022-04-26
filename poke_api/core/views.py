from django.shortcuts import render
from .utils.pokemons.factory import make_pokemons

def home(request):
    return render(request,'pokemons/pages/home.html',context={
        'pokemons' : [make_pokemons() for _ in range(10)]
    })

def poke(request,id):
    return render(request,'pokemons/pages/poke-view.html',context={
        'pokemon' : make_pokemons,
        'is_detail_page' : True
    })

# Create your views here.
