# Generated by Django 5.1.4 on 2025-01-13 13:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
        ('movies', '0002_genre_alter_movie_options_remove_movie_genre_ids_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumpost',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forum_posts', to='movies.movie'),
        ),
    ]
