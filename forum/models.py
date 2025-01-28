from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie
from django.utils.text import slugify

STATUS = ((0, "Draft"), (1, "Published"))

class ForumPost(models.Model):
    """
    Model to represent a forum post.

    Data is obtained from:
    - User input through forms and the Movie model.

    Data is returned as:
    - A ForumPost instance with attributes like title, content, author, etc.
    """
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    upvotes = models.ManyToManyField(User, related_name='forum_post_upvotes', blank=True)
    downvotes = models.ManyToManyField(User, related_name='forum_post_downvotes', blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    approved_post = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        """
        Save the forum post instance. Generates a unique slug if not provided.
        """
        if not self.slug:
            self.slug = slugify(f"{self.movie.slug}-{self.title}")
            original_slug = self.slug
            queryset = ForumPost.objects.filter(slug=self.slug).exists()
            counter = 1
            while queryset:
                self.slug = f"{original_slug}-{counter}"
                counter += 1
                queryset = ForumPost.objects.filter(slug=self.slug).exists()
        super().save(*args, **kwargs)
    
    @property
    def published_comment_count(self):
        """
        Returns the count of published comments for the forum post.
        """
        return self.comments.filter(approved_comment=True).count()


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Movie: {self.movie}  -  {self.title}  by  {self.author} on  {self.created_at}"

class PostComment(models.Model):
    """
    Model to represent a comment on a forum post.

    Data is obtained from:
    - User input through forms and the ForumPost model.

    Data is returned as:
    - A PostComment instance with attributes like comment, author, etc.
    """
    forum_post = models.ForeignKey(ForumPost, on_delete=models.CASCADE, related_name='comments',)  # Temporarily make it nullable
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_author')
    comment = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"{self.forum_post}  by  {self.author}  on  {self.comment}  at  {self.created_at}"