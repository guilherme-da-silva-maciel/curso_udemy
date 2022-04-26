from django.urls import path
from . import views

app_name = 'pokedex'

urlpatterns = [
    path('',views.home,name='home'),
    path('poke/<int:id>/',views.poke,name='pokemon')
]
