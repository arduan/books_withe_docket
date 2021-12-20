from django.db import models

from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    text = models.TextField("Текст")

    def __str__(self):
        return f'{self.title} {self.text}'
