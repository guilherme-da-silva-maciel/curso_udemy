from django.urls import path 
from . import views


app_name = 'authors'

urlpatterns = [
    path('register/',views.register_view,name='register'),
    path('register/create',views.create_view,name='create'),
    path('login/',views.login_view,name='login'),
    path('login/create',views.login_create,name='login_create'),
    path('logout/',views.logout_view,name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('dashboard/pokemon/<int:id>/edit/',views.dashboard_pokemon_edit,name='dash_edit'),
    path('dashboard/pokemon/new',views.dashboard_pokemon_new,name='dashboard_pokemon_new'),
    path('dashboard/pokemon/<int:id>/delete/',views.dashboard_pokemon_delete,name='dash_delete')
]
