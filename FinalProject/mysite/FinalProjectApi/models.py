from django.db import models
from django.db.models import CharField
from django.utils import timezone
from django.conf import settings
from django.contrib import admin


class Game(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    launching_date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> CharField:
        return self.name
