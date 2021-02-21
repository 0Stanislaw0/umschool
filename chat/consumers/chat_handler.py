import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from chat.models import Message
from lessons.models import Lesson


class ChatMessageHandler(AsyncWebsocketConsumer):
    """
    Класс для обработки веб сокетов
    """

    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["lesson_id"]
        self.room_group_name = "chat_%s" % self.room_name

        if self.scope["user"].is_authenticated:
            self.chat = await self._get_chat()
            if self.chat:
                await self.channel_layer.group_add(
                    self.room_group_name, self.channel_name
                )

                await self.accept()
            else:
                await self.close(code=404)
        else:
            await self.close(code=401)

    @database_sync_to_async
    def _get_chat(self):
        return Lesson.objects.filter(
            pk=self.room_name, users__in=[self.scope["user"]]
        ).first()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    @database_sync_to_async
    def _create_message(self, message):
        Message.objects.create(
            author=self.scope["user"], lesson=self.chat, context=message
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        await self._create_message(message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "user": self.scope["user"].username,
                "message": message,
            },
        )

    async def chat_message(self, event):
        message = event["message"]
        user = event["user"]

        await self.send(text_data=json.dumps({"message": message, "user": user}))
