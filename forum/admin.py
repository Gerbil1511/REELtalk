from django.contrib import admin
from .models import ForumPost, PostComment

# Register your models here.
@admin.register(ForumPost)
class ForumPostAdmin(admin.ModelAdmin):
    list_display = ('title',  'author', 'movie', 'approved_post', 'status', 'created_at', 'slug')
    search_fields = ('title', 'author', 'movie', 'created_at')
    list_filter = ('author', 'movie', 'created_at', 'approved_post', 'status',)

    def total_upvotes(self, obj):
        return obj.upvotes.count()
    total_upvotes.short_description = 'Upvotes'

    def total_downvotes(self, obj):
        return obj.downvotes.count()
    total_downvotes.short_description = 'Downvotes'


@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('forum_post', 'author', 'comment', 'approved_comment', 'status', 'created_at')
    search_fields = ('forum_post', 'author', 'comment', 'created_at', )
    list_filter = ('author', 'created_at', 'approved_comment', 'status',)  # Add fields to filter by


