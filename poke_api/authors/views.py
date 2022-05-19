from django.urls import reverse
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import Register_user,LoginForm,AuthorPokemonForm
from django.http import Http404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from core.models import Pokedex

def register_view(request):
    register_form_data = request.session.get('register_form_data',None)
    form = Register_user(register_form_data)
    return render(request,'pages/register_view.html',{
        'form' : form
    })
    
def create_view(request):
    if not request.POST:
        raise Http404


    POST = request.POST

    request.session['register_form_data'] = POST

    form = Register_user(POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()

        
        messages.success(request,'your user is created! , please log in.')

        del(request.session['register_form_data'])
        return redirect(reverse('authors:login'))

    return redirect('authors:register')


def login_view(request):
    form = LoginForm()
    return render (request,'pages/login_view.html',{
        'form' : form,
        'form_action' : reverse('authors:login_create')
    })

def login_create(request):
    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)
    login_url = reverse('authors:login')

    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )

        if authenticated_user is not None:
            messages.success(request, 'Your are logged in.')
            login(request, authenticated_user)
        else:
            messages.error(request, 'Invalid credentials')
    else:
        messages.error(request, 'Invalid username or password')

    return redirect(login_url)

@login_required(login_url='authors:login',redirect_field_name='next')
def logout_view(request):
    if not request.POST:
        return redirect(reverse('authors:login'))

    if request.POST.get('username') != request.user.username:
        return redirect(reverse('authors:login'))


    logout(request)
    return redirect(reverse('authors:login'))


@login_required(login_url='authors:login',redirect_field_name='next')
def dashboard(request):
    pokemons = Pokedex.objects.filter(
        is_published=False,
        hunter=request.user
    )
    return render(request,'pages/dashboard.html',context={
        'pokemons' : pokemons
    })

@login_required(login_url='authors:login',redirect_field_name='next')
def dashboard_pokemon_edit(request,id):
    pokemon = Pokedex.objects.filter(
        is_published=False,
        hunter=request.user,
        pk=id
    ).first()

    if not pokemon:
        raise Http404

    form = AuthorPokemonForm(
        request.POST or None,
        instance=pokemon
    )

    return render(request,'pages/dashboard_pokemon.html',context={
        'form' : form
    })
# Crea
# Create your views here.
