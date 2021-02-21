from django.db import models

from lessons.models import Lesson
from users.models import User


class Message(models.Model):
    author = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    lesson = models.ForeignKey(
        Lesson, related_name="messages", on_delete=models.CASCADE
    )
    context = models.TextField("Сообщение")
    created_at = models.DateTimeField("Создано", auto_now_add=True)

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
