from django.db import models

from users.models import User


class Lesson(models.Model):
    name = models.CharField("Название", max_length=50)
    users = models.ManyToManyField(
        User, verbose_name="Пользователи", related_name="lessons"
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return self.name
