from django.contrib.auth.models import AbstractUser
from django.db import models

from users.orm_managers.user_manager import UserManager


class User(AbstractUser):
    objects = UserManager()

    email = models.EmailField('Электронная почта', unique=True)

    REQUIRED_FIELDS = ['first_name', 'last_name']
    USERNAME_FIELD = 'email'

    first_name = models.CharField('Имя', max_length=255)
    last_name = models.CharField('Фамилия', max_length=255)

    username = None

