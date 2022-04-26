from django.db import models
from django.contrib.auth.models import User

class Type(models.Model) :
    tipo = models.CharField(max_length=65)

class Pokedex(models.Model) :
    name = models.CharField(max_length=65)
    desciption = models.CharField(max_length=165)
    slug = models.SlugField()
    rarity = models.CharField(max_length=20)
    mega_form = models.BooleanField()
    base_stats = models.TextField()
    base_stats_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='pokemons/covers/%y/%m/%d')
    type = models.ForeignKey(Type,on_delete=models.SET_NULL,null=True)
    hunter = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)


# Create your models here.
