from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class Tipo(models.Model) :
    tipo = models.CharField(max_length=65)
    def __str__(self):
        return self.tipo

class Tipo_2(models.Model):
    tipo_2 = models.CharField(max_length=65)
    def __str__(self):
        return self.tipo_2

class Pokedex(models.Model) :
    name = models.CharField(max_length=65)
    desciption = models.CharField(max_length=165)
    slug = models.SlugField()
    rarity = models.CharField(max_length=20)
    mega_form = models.BooleanField()
    base_stats = models.ImageField(upload_to='pokemons/covers/%y/%m/%d')
    base_stats_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='pokemons/covers/%y/%m/%d',blank=True,default='')
    tipo = models.ForeignKey(Tipo,on_delete=models.SET_NULL,null=True,blank=True,default=None)
    tipo_2 =  models.ForeignKey(Tipo_2,on_delete=models.SET_NULL,null=True,blank=True,default=None)
    hunter = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.name


# Create your models here.
