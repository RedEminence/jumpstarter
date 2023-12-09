# Generated by Django 4.2.7 on 2023-12-09 16:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='Сумма для сбора')),
                ('current_amount', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='Текущая собранная сумма')),
                ('deadline', models.DateTimeField(verbose_name='Дедлайн')),
                ('status', models.CharField(choices=[('Профинансирован', 'funded'), ('В процесе финансирования', 'in_progress'), ('Отменен', 'cancelled')], verbose_name='Статус')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]