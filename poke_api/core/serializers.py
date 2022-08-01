from typing import DefaultDict
from rest_framework import serializers


from .models import Pokedex, Tipo

class Tipo_serializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = ['tipo']
    tipo = serializers.CharField()


class Poke_serializer(serializers.ModelSerializer):
    class Meta:
        model = Pokedex
        fields = ['id','name','tipo','rarity','dono','public','desciption','tipo','mega_form']
    tipo = serializers.SerializerMethodField()
    dono = serializers.CharField(source='hunter',read_only=True)
    public = serializers.BooleanField(source='is_published',read_only=True)
    mega_form = serializers.BooleanField()


    def get_tipo(self,pokedex):
        if pokedex.tipo_2 is None:
            return (f'{pokedex.tipo}')
        else:
            return (f'{pokedex.tipo},{pokedex.tipo_2}')

    def validate(self, attrs):
        super_validate = super().validate(attrs)

        cd = attrs

        erros = DefaultDict(list)

        name = cd.get('name')
        rarity = cd.get('rarity')

        if name == rarity:
            erros['name'].append('name cannot equal rarity')
            erros['dono'].append('rarity cannot equal name')

        if erros:
            raise serializers.ValidationError(erros)

        return super_validate
        