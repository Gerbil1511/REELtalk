from django.contrib import admin
from .models import ForumPost

# Register your models here.
@admin.register(ForumPost)
class ForumPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'movie', 'created_at', 'total_upvotes', 'total_downvotes')
    search_fields = ('title', 'content', 'author__username', 'movie__title')
    list_filter = ('author', 'movie', 'created_at')  # Add fields to filter by
    
    def total_upvotes(self, obj):
        return obj.upvotes.count()
    total_upvotes.short_description = 'Upvotes'

    def total_downvotes(self, obj):
        return obj.downvotes.count()
    total_downvotes.short_description = 'Downvotes'