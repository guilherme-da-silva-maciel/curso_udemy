from django.urls import path
from . import views

app_name = 'pokedex'

urlpatterns = [
    path('poke/search/',views.search,name='search'),
    path('',views.home,name='home'),
    path('poke/type/<int:tipo_id>/',views.tipo,name='tipo'),
    path('poke/<int:id>/',views.poke,name='pokemon')
]
