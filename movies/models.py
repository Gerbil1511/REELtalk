from django.db import models

# Create your models here.
class Movie(models.Model):
    tmdb_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)  # Add slug field
    release_date = models.DateField()
    poster_path = models.CharField(max_length=255)
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    popularity = models.FloatField()
    genre_ids = models.CharField(max_length=255)  # Store genre IDs as a comma-separated string
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            unique_slug = self.slug
            num = 1
            while Movie.objects.filter(slug=unique_slug).exists():
                unique_slug = f'{self.slug}-{num}'
                num += 1
            self.slug = unique_slug
        super(Movie, self).save(*args, **kwargs)
        
    class Meta:
        ordering = ['-release_date']  # Order by release date, newest first

    def __str__(self):
        return self.title
