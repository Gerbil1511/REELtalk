from django.contrib import admin
from .models import ForumPost

# Register your models here.
@admin.register(ForumPost)
class ForumPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'movie', 'created_at', 'updated_at', 'total_upvotes', 'total_downvotes')
    search_fields = ('title', 'content', 'author__username', 'movie__title')