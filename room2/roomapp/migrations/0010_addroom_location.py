# Generated by Django 4.1.2 on 2022-12-08 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomapp', '0009_alter_addroom_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='addroom',
            name='location',
            field=models.TextField(default=1, max_length=100),
        ),
    ]
