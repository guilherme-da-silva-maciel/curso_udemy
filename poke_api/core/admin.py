from django.contrib import admin
from .models import Pokedex, Tipo, Tipo_2

class TipoAdmin(admin.ModelAdmin) :
    ...

@admin.register(Pokedex)
class PokedexAdmin(admin.ModelAdmin) :
    ...


admin.site.register(Tipo,admin.ModelAdmin)

admin.site.register(Tipo_2,admin.ModelAdmin)
# Register your models here.
