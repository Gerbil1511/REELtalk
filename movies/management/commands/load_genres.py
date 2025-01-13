import json
from django.core.management.base import BaseCommand
from movies.models import Genre

class Command(BaseCommand):
    help = 'Load genres from a JSON file into the Genre model'

    def handle(self, *args, **kwargs):
        with open('movies/management/commands/genres.json', 'r') as file:
            genres_data = json.load(file)
            for genre_item in genres_data['genres']:
                Genre.objects.get_or_create(
                    tmdb_id=genre_item['id'],
                    defaults={'name': genre_item['name']}
                )
        self.stdout.write(self.style.SUCCESS('Successfully loaded genres'))