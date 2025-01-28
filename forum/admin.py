from django.contrib import admin
from .models import ForumPost, PostComment

# Register your models here.
@admin.register(ForumPost)
class ForumPostAdmin(admin.ModelAdmin):
    """
    Admin view for managing ForumPost instances.

    Data is obtained from:
    - ForumPost model: Retrieves forum post instances.

    Data is returned as:
    - Admin interface for managing forum posts.
    """
    list_display = ('title',  'author', 'movie', 'approved_post', 'status', 'created_at', 'slug')
    search_fields = ('title', 'author', 'movie', 'created_at')
    list_filter = ('author', 'movie', 'created_at', 'approved_post', 'status',)

    def total_upvotes(self, obj):
        """
        Returns the total number of upvotes for a forum post.

        Args:
            obj (ForumPost): The forum post instance.

        Returns:
            int: The total number of upvotes.
        """
        return obj.upvotes.count()
    total_upvotes.short_description = 'Upvotes'

    def total_downvotes(self, obj):
        """
        Returns the total number of downvotes for a forum post.

        Args:
            obj (ForumPost): The forum post instance.

        Returns:
            int: The total number of downvotes.
        """
        return obj.downvotes.count()
    total_downvotes.short_description = 'Downvotes'


@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    """
    Admin view for managing PostComment instances.

    Data is obtained from:
    - PostComment model: Retrieves post comment instances.

    Data is returned as:
    - Admin interface for managing post comments.
    """
    list_display = ('forum_post', 'author', 'comment', 'approved_comment', 'status', 'created_at')
    search_fields = ('forum_post', 'author', 'comment', 'created_at', )
    list_filter = ('author', 'created_at', 'approved_comment', 'status',)  # Add fields to filter by


