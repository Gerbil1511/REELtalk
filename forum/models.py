from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie

# Create your models here.

class ForumPost(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Track when the post was last updated
    upvotes = models.ManyToManyField(User, related_name='forum_post_upvotes', blank=True)
    downvotes = models.ManyToManyField(User, related_name='forum_post_downvotes', blank=True)

    def __str__(self):
        return self.title

    def total_upvotes(self):
        return self.upvotes.count()

    def total_downvotes(self):
        return self.downvotes.count()