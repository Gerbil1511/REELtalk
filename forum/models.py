from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie
from django.utils.text import slugify

STATUS = ((0, "Draft"), (1, "Published"))

class ForumPost(models.Model):
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

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Movie: {self.movie}  -  {self.title}  by  {self.author} on  {self.created_at}"

class PostComment(models.Model):
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