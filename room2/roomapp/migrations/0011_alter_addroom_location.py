# Generated by Django 4.1.2 on 2022-12-08 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomapp', '0010_addroom_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addroom',
            name='location',
            field=models.TextField(max_length=100),
        ),
    ]
