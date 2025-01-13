from django.contrib import admin
from .models import Movie, Genre

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'vote_average', 'vote_count', 'get_genres')
    search_fields = ('title', 'genres__name')  # Use the related field lookup for genres

    def get_genres(self, obj):
        return ", ".join([genre.name for genre in obj.genres.all()])
    get_genres.short_description = 'Genres'

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)