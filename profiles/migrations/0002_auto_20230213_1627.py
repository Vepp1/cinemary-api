# Generated by Django 3.2.16 on 2023-02-13 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='biography',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
    ]