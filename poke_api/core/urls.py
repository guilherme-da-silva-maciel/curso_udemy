from atexit import register
from django.db import router
from django.urls import include, path , re_path
from core import views
from rest_framework.routers import SimpleRouter
import oauth2_provider

pokemon_router = SimpleRouter()

pokemon_router.register('poke/api',views.PokeViewset,basename='poke-api')

tipo_router = SimpleRouter()

tipo_router.register('poke/api/tipo',views.TipoViewset,basename='tipo-api')


app_name = 'pokedex'


urlpatterns = [
    path('',views.home,name='home'),
    path('poke/search/',views.search,name='search'),
    path('poke/type/<int:tipo_id>/',views.tipo,name='tipo'),
    path('poke/<int:id>/',views.poke,name='pokemon'),
    path(r'o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('',include(pokemon_router.urls)),
    path('',include(tipo_router.urls))
]
