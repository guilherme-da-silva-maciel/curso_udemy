from django.contrib import admin
from .models import Pokedex, Tipo, Tipo_2

class TipoAdmin(admin.ModelAdmin) :
    ...

@admin.register(Pokedex)
class PokedexAdmin(admin.ModelAdmin) :
    list_display = ['id','name','created_at','is_published']
    list_display_links = 'name','created_at'
    search_fields = 'id','name','desciption','slug',
    list_filter = ['tipo','hunter','is_published']
    list_per_page = 10
    list_editable = ['is_published']
    ordering = ['-id']
    prepopulated_fields = {
        "slug" : ("name",)
    }


admin.site.register(Tipo,admin.ModelAdmin)

admin.site.register(Tipo_2,admin.ModelAdmin)
# Register your models here.
