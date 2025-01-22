from django.contrib import admin
from .models import Movie 

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'release_date', 'genre_ids', 'vote_count', 'vote_average',)
    search_fields = ('title', 'release_date', 'vote_average')  
    list_filter = ('title', 'release_date',)  # Add fields to filter by