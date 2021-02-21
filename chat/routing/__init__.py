from django.urls import re_path

from chat.consumers.chat_handler import ChatMessageHandler

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<lesson_id>\w+)/", ChatMessageHandler.as_asgi())
]
