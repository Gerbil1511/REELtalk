from django.contrib import admin
from .models import Movie 

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """
    Admin view for managing Movie instances.

    Data is obtained from:
    - Movie model: Retrieves movie instances.

    Data is returned as:
    - Admin interface for managing movies.
    """
    list_display = ('title', 'slug', 'release_date', 'genre_ids', 'vote_count', 'vote_average',)
    search_fields = ('title', 'release_date', 'vote_average')  
    list_filter = ('title', 'release_date',)  # Add fields to filter by