# Generated by Django 4.1.1 on 2022-12-01 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomapp', '0002_addroom'),
    ]

    operations = [
        migrations.AddField(
            model_name='addroom',
            name='room_type',
            field=models.CharField(default='s', max_length=20, verbose_name='roomtype'),
        ),
    ]
