# Generated by Django 3.2.16 on 2023-07-25 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_posts_actors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='genre',
            field=models.CharField(max_length=25),
        ),
    ]
