# Generated by Django 5.1.4 on 2025-01-13 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_genre_alter_movie_options_remove_movie_genre_ids_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='popularity',
        ),
    ]
