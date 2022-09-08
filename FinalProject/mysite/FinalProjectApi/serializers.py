from rest_framework import serializers
from .models import *


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'name', 'genre', 'launching_date')

