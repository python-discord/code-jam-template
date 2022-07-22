from django.urls import path
from .consumers import GameConsumer
from django.urls import re_path


ws_urlpatterns = [
    re_path(r'ws/game/(?P<game_id>\w+)/$',GameConsumer.as_asgi()),
]