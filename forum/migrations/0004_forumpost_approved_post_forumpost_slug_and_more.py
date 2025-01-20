# Generated by Django 5.1.4 on 2025-01-20 18:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_alter_forumpost_options'),
        ('movies', '0006_remove_movie_genres_alter_movie_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='forumpost',
            name='approved_post',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='forumpost',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='forumpost',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
        migrations.AlterField(
            model_name='forumpost',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='forumpost',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_movie', to='movies.movie'),
        ),
        migrations.AlterField(
            model_name='forumpost',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('approved_comment', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_author', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='original_post', to='forum.forumpost')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
