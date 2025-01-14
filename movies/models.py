from django.db import models

# Create your models here.

class Genre(models.Model):
    tmdb_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    tmdb_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    overview = models.TextField(blank=True)
    release_date = models.DateField(blank=True, null=True)  # Allow null values
    poster_path = models.CharField(max_length=255, blank=True, null=True)  # Allow null values
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    genres = models.ManyToManyField(Genre, related_name="movies")

    class Meta:
        ordering = ['-release_date']

    def __str__(self):
        return self.title
