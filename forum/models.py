from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie

# Create your models here.

class ForumPost(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='forum_posts')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Track when the post was last updated
    upvotes = models.ManyToManyField(User, related_name='forum_post_upvotes', blank=True)
    downvotes = models.ManyToManyField(User, related_name='forum_post_downvotes', blank=True)

    class Meta:
        ordering = ['-created_at']  # Order by creation date, newest first
        
    def __str__(self):
        return self.title

    def total_upvotes(self):
        return self.upvotes.count()

    def total_downvotes(self):
        return self.downvotes.count()
    
    def upvote(self, user):
        if user == self.author:
            return  # Prevent the author from upvoting their own post
        if user in self.downvotes.all():
            self.downvotes.remove(user)
        if user not in self.upvotes.all():
            self.upvotes.add(user)

    def downvote(self, user):
        if user == self.author:
            return  # Prevent the author from downvoting their own post
        if user in self.upvotes.all():
            self.upvotes.remove(user)
        if user not in self.downvotes.all():
            self.downvotes.add(user)