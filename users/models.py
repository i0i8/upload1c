from django.db import models
from django.contrib.auth.models import AbstractUser


class Role(models.TextChoices):

    MANAGER = 'MANAGER', 'Менеджер'
    LOGIST = 'LOGIST', 'Логист'
    SUPERVISOR_LOGIST = 'SUPERVISOR', 'Руководитель логистики'
    DRIVER = 'DRIVER', 'Водитель'

class User(AbstractUser):
    role = models.CharField(max_length=15, choices=Role.choices)

    def __srt__(self):
        return self.username


