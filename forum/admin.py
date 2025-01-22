from django.contrib import admin
from .models import ForumPost, PostComment

# Register your models here.
@admin.register(ForumPost)
class ForumPostAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'movie', 'title', 'created_at', 'updated_at', 'approved_post')
    search_fields = ('movie', 'author', 'author__username', 'movie__title', 'status', 'approved_post')
    list_filter = ('author', 'movie', 'created_at', 'updated_at', 'status', 'approved_post')  # Add fields to filter by
    
    def total_upvotes(self, obj):
        return obj.upvotes.count()
    total_upvotes.short_description = 'Upvotes'

    def total_downvotes(self, obj):
        return obj.downvotes.count()
    total_downvotes.short_description = 'Downvotes'


@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'author', 'post', 'created_at', 'approved_comment')
    search_fields = ('post', 'author', 'comment', 'created_at', 'approved_comment')
    list_filter = ('author', 'created_at', 'approved_comment')  # Add fields to filter by

