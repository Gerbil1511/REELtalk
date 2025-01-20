from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))


class ForumPost(models.Model):
    """
    Model to represent a forum post.
    """
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='related_movie')
    slug = models.SlugField(max_length=255, unique=True, blank=True)  # Allow blank slugs initially
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField(default='')  # Provide a default value
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    upvotes = models.ManyToManyField(User, related_name='forum_post_upvotes', blank=True)
    downvotes = models.ManyToManyField(User, related_name='forum_post_downvotes', blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    approved_post = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Movie: {self.movie}  -  {self.title}  by  {self.author} on  {self.created_at}"

class PostComment(models.Model):
    """
    Model to represent a comment on a forum post.
    """
    post = models.ForeignKey(ForumPost, on_delete=models.CASCADE, related_name='original_post')  # Related post
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_author')  # Comment author
    comment = models.TextField(default='') 
    created_at = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_at']       

    def __str__(self):      
        return f"{self.comment}  by  {self.author}  on  {self.post}  at  {self.created_at}"