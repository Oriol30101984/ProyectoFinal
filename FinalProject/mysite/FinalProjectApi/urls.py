from django.urls import include, path
from rest_framework import routers
from . import views


GameRouter = routers.DefaultRouter()
PartyRouter = routers.SimpleRouter()
PartyMessageRouter = routers.SimpleRouter()
GameRouter.register(r'juegos', views.GameViewSet)
PartyRouter.register(r'grupos', views.PartyViewSet)
PartyMessageRouter.register(r'mensajes', views.PartyMessageViewSet)

urlpatterns = [
    path('', include(GameRouter.urls)),
    path('', include(PartyRouter.urls)),
    path('', include(PartyMessageRouter.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
