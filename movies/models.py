from django.db import models
from django.utils.text import slugify

# Create your models here.


class Movie(models.Model):
    """
    Model to represent a movie.
    """
    poster_path = models.CharField(max_length=255, default='no_poster_for_movie.webp')  
    title = models.CharField(max_length=255)
    tmdb_id = models.IntegerField(unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)  # allows the slug to be empty initially, so it can be generated in the save method
    genre_ids = models.JSONField(default=list)
    release_date = models.DateField(default='1900-01-01')  # Provide a default value
    overview = models.TextField(default='No overview available')  # Provide a default value
    popularity = models.FloatField(default=0.0)
    vote_count = models.IntegerField(default=0)  # Provide a default value
    vote_average = models.FloatField(default=0.0)  # Provide a default value

    def save(self, *args, **kwargs):
        """
        Override the save method to generate a unique slug if not already set.
        """
        if not self.slug:
            self.slug = slugify(f"{self.title}-{self.tmdb_id}")  # Generate slug from title and TMDb ID
        super().save(*args, **kwargs)  # Call the original save method

    def __str__(self):
        return f"{self.title}  |  {self.release_date}  |  {self.genre_ids}"
    
