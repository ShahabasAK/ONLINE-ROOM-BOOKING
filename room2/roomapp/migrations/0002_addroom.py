# Generated by Django 4.1.1 on 2022-12-01 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.IntegerField()),
                ('room_name', models.CharField(max_length=100, verbose_name='First name')),
                ('photo', models.ImageField(upload_to='images/', verbose_name='Photo')),
                ('rate', models.CharField(max_length=100, verbose_name='Rate')),
                ('discription', models.CharField(max_length=25, verbose_name='Discription')),
            ],
        ),
    ]
