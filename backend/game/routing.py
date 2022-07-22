from django.urls import path, re_path
from .consumers import GameConsumer


ws_urlpatterns = [
    re_path(r'ws/game/(?P<game_id>\w+)/$',GameConsumer.as_asgi()),
]
