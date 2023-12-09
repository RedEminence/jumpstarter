import os

# Установка ссылки на конфиг приложения
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jumpstarter.settings")

from django import db

with db.connection.cursor() as cursor:
    cursor.execute('SELECT * FROM public.users_user')
    print(cursor.fetchall())
