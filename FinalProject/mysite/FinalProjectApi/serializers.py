from dataclasses import fields
from rest_framework import serializers
from .models import *


class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ('name', 'genre', 'launching_date')


class PartySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Party
        fields = ('name', 'game', 'creation_date')


class PartyMessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PartyMessage
        fields = ('user', 'content', 'deleted', 'creation_date', 'updated_date')