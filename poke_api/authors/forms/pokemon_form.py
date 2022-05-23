
from django import forms
from core.models import Pokedex
from authors.utils.django_form import add_attr
from collections import defaultdict


class AuthorRecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._my_errors = defaultdict(list)


        add_attr(self.fields.get('cover'), 'class', 'span-2')


class AuthorPokemonForm(forms.ModelForm):
    class Meta:
        model = Pokedex
        fields = ['name','desciption','rarity','mega_form','base_stats','base_stats_is_html','cover','tipo','tipo_2']


    


    def clean(self,*args, **kwargs):
        super_clean = super().clean(*args, **kwargs)
        cd = self.cleaned_data

        

        return super_clean