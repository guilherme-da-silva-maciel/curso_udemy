from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('poke/<int:id>/',views.poke)
]
