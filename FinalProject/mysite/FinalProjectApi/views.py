from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all().order_by('name')
    serializer_class = GameSerializer


class PartyViewSet(viewsets.ModelViewSet):
    queryset = Party.objects.all().order_by('name')
    serializer_class = PartySerializer


class PartyMessageViewSet(viewsets.ModelViewSet):
    queryset = PartyMessage.objects.all().order_by('creation_date')
    serializer_class = PartyMessageSerializer
