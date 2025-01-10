from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    tmdb_id = models.IntegerField(unique=True)
    overview = models.TextField()
    release_date = models.DateField()
    poster_path = models.CharField(max_length=255)
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    popularity = models.FloatField()
    genre_ids = models.CharField(max_length=255)  # Store genre IDs as a comma-separated string
    director = models.CharField(max_length=255)  # Add director field
    main_actors = models.CharField(max_length=255)  # Add main actors field

    def __str__(self):
        return self.title
