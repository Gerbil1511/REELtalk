from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
from .models import ForumPost, PostComment
from movies.models import Movie
from .forms import PostCommentForm, ForumPostForm
import requests

def forum_post_list(request):
    """
    View to list all forum posts. Allows searching by movie title.
    """
    search_query = request.GET.get('search', '')
    forum_posts = ForumPost.objects.filter(status=1)  # Only show published posts

    if search_query:
        # Filter forum posts by movie title
        forum_posts = forum_posts.filter(movie__title__icontains=search_query)

    paginator = Paginator(forum_posts, 10)  # Show 10 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'forum/forum_post_list.html', {
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
        'search_query': search_query,
    })

def forum_post_detail(request, id):
    """
    View to display the details of a single forum post, including comments.
    Allows logged-in users to submit comments.
    """
    post = get_object_or_404(ForumPost, id=id, status=1)  # Get the post or return 404 if not found
    comments = post.original_post.filter(approved_comment=True).order_by('-created_at')  # Get approved comments
    comment_count = comments.count()

    if request.method == 'POST':
        # If the request method is POST, process the comment form
        comment_form = PostCommentForm(data=request.POST)
        if comment_form.is_valid():
            # If the form is valid, save the comment but don't commit to the database yet
            comment = comment_form.save(commit=False)
            # Associate the comment with the post and the current user
            comment.post = post
            comment.author = request.user
            # Save the comment to the database
            comment.save()
            messages.success(request, 'Comment submitted and awaiting approval')
            # Redirect to the same post detail page
            return redirect('forum_post_detail', id=post.id)
    else:
        # If the request method is GET, create an empty comment form
        comment_form = PostCommentForm()

    return render(request, 'forum/forum_post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'comment_count': comment_count
    })

@login_required
def upvote_post(request, id):
    """
    View to handle upvoting a forum post. Only accessible to logged-in users.
    """
    post = get_object_or_404(ForumPost, id=id)  # Get the post or return 404 if not found
    post.upvotes.add(request.user)  # Add the current user to the upvotes
    post.downvotes.remove(request.user)  # Remove the current user from the downvotes
    return redirect('forum_post_list')  # Redirect to the forum post list

@login_required
def downvote_post(request, id):
    """
    View to handle downvoting a forum post. Only accessible to logged-in users.
    """
    post = get_object_or_404(ForumPost, id=id)  # Get the post or return 404 if not found
    post.downvotes.add(request.user)  # Add the current user to the downvotes
    post.upvotes.remove(request.user)  # Remove the current user from the upvotes
    return redirect('forum_post_list')  # Redirect to the forum post list

@login_required
def edit_comment(request, comment_id):
    """
    View to edit a comment. Only accessible to the comment's author.
    """
    # Get the comment or return 404 if not found or if the user is not the author
    comment = get_object_or_404(PostComment, id=comment_id, author=request.user)
    
    if request.method == 'POST':
        # If the request method is POST, process the comment form
        comment_form = PostCommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            # If the form is valid, save the updated comment
            comment_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment updated successfully'
            )
            # Redirect to the post detail page
            return redirect('forum_post_detail', id=comment.post.id)
    else:
        # If the request method is GET, create a form with the existing comment data
        comment_form = PostCommentForm(instance=comment)
    
    # Render the edit comment template with the comment form
    return render(request, 'forum/edit_comment.html', {'comment_form': comment_form})

@login_required
def delete_comment(request, comment_id):
    """
    View to delete a comment. Only accessible to the comment's author.
    """
    # Get the comment or return 404 if not found or if the user is not the author
    comment = get_object_or_404(PostComment, id=comment_id, author=request.user)
    post_id = comment.post.id  # Store the post ID to redirect after deletion
    comment.delete()  # Delete the comment
    messages.add_message(
        request, messages.SUCCESS,
        'Comment deleted successfully'
    )
    # Redirect to the post detail page
    return redirect('forum_post_detail', id=post_id)

def movie_detail(request, tmdb_id):
    """
    View to display the details of a single movie.
    """
    movie = get_object_or_404(Movie, tmdb_id=tmdb_id)  # Get the movie or return 404 if not found
    return render(request, 'movies/movie_detail.html', {'movie': movie})
