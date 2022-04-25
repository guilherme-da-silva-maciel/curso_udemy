from django.shortcuts import render

def home(request):
    return render(request,'pokemons/pages/home.html',context={'name' : 'darkrai'})

def poke(request,id):
    return render(request,'pokemons/pages/poke-view.html',context={'name' : 'darkrai'})

# Create your views here.
