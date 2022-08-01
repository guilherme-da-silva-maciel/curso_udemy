from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from ..models import Pokedex, Tipo
from rest_framework import status
from ..serializers import Poke_serializer, Tipo_serializer
from rest_framework.viewsets import ModelViewSet
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, OAuth2Authentication
from rest_framework.authentication import SessionAuthentication 
from rest_condition import Or
from rest_framework.permissions import IsAdminUser


class PokeViewset(ModelViewSet):
    queryset = Pokedex.objects.get_published()
    serializer_class = Poke_serializer
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [Or(IsAdminUser, TokenHasReadWriteScope)]

class TipoViewset(ModelViewSet):
    queryset = Tipo.objects.all()
    serializer_class = Tipo_serializer
    