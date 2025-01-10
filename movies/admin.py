from django.contrib import admin
from .models import Movie

# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'vote_average', 'vote_count', 'popularity', 'director', 'main_actors')
    search_fields = ('title', 'overview', 'director', 'main_actors')
