from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib import admin


class ProjectModel(admin.ModelAdmin):
    def has_add_permission(request) -> bool:
        return True

    def has_change_permission(request, obj=None) -> bool:
        return False

    def has_delete_permission(request, obj=None) -> bool:
        return False


class Game(ProjectModel):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    launching_date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.name


class Party(ProjectModel):
    name = models.CharField(max_length=100)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.name


class PartyMessage(ProjectModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField()
    deleted = models.BooleanField()
    creation_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

    def has_change_permission(request, obj=None) -> bool:
        if not obj: return False

        return settings.AUTH_USER_MODEL == obj.user

    def has_delete_permission(request, obj=None) -> bool:
        if not obj: return False

        return settings.AUTH_USER_MODEL == obj.user

    def __str__(self) -> str:
        return self.content
