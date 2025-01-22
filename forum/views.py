
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings 
from .models import ForumPost, PostComment
from movies.models import Movie 
from .forms import PostCommentForm, ForumPostForm
import requests


def forum_post_list(request):
    # Ensure the form for creating a new post is handled correctly.
    if request.method == 'POST':
        form = ForumPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('forum_post_list')
    else:
        form = ForumPostForm()

    # TMDB API search
    search_query = request.GET.get('search', '')
    tmdb_results = []
    if search_query:
        tmdb_api_key = settings.TMDB_API_KEY
        tmdb_url = f'https://api.themoviedb.org/3/search/movie?api_key={tmdb_api_key}&query={search_query}'
        response = requests.get(tmdb_url)
        if response.status_code == 200:
            tmdb_results = response.json().get('results', [])

    # Get all published forum posts
    post_list = ForumPost.objects.filter(status=1)
    paginator = Paginator(post_list, 10)  # Show 10 posts per page

    # Get the current page number from the request
    page_number = request.GET.get('page')
    # Get the page object for the current page
    page_obj = paginator.get_page(page_number)

    # Render the forum post list template with the page object and pagination status
    return render(request, 'forum/forum_post_list.html', {
                'page_obj': page_obj,
                'is_paginated': page_obj.has_other_pages(),
                'form': form,
                'tmdb_results': tmdb_results,
                })


@login_required
def upvote_post(request, id):
    post = get_object_or_404(ForumPost, id=id)
    post.upvotes.add(request.user)
    # Ensure user can't upvote and downvote at the same time
    post.downvotes.remove(request.user)
    return redirect('forum_post_list')


@login_required
def downvote_post(request, id):
    post = get_object_or_404(ForumPost, id=id)
    post.downvotes.add(request.user)
    # Ensure user can't upvote and downvote at the same time
    post.upvotes.remove(request.user)
    return redirect('forum_post_list')


def forum_post_detail(request, id):
    # Get the forum post with the given ID and status 1 (published)
    queryset = ForumPost.objects.filter(status=1)
    post = get_object_or_404(queryset, id=id)
    # Get all approved comments for the post, ordered by creation date
    comments = post.original_post.filter(
        approved_comment=True).order_by("-created_at")
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
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
            # Redirect to the same post detail page
            return redirect('forum_post_detail', id=post.id)
    else:
        # If the request method is GET, create an empty comment form
        comment_form = PostCommentForm()

    # Render the forum post detail template with the post, comments, comment form, and comment count
        return render(
            request,
            'forum/forum_post_detail.html',
            {
                'post': post,
                'comments': comments,
                'comment_form': comment_form,
                'comment_count': comment_count
            },
        )


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(
        PostComment, id=comment_id, author=request.user)
    if request.method == 'POST':
        comment_form = PostCommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment updated successfully'
            )
            return redirect('forum_post_detail', id=comment.post.id)
    else:
        comment_form = PostCommentForm(instance=comment)
    return render(request, 'forum/edit_comment.html', {'comment_form': comment_form})


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(
        PostComment, id=comment_id, author=request.user)
    post_id = comment.post.id
    comment.delete()
    messages.add_message(
        request, messages.SUCCESS,
        'Comment deleted successfully'
    )
    return redirect('forum_post_detail', id=post_id)

def movie_detail(request, tmdb_id):
    tmdb_api_key = settings.TMDB_API_KEY
    tmdb_url = f'https://api.themoviedb.org/3/movie/{tmdb_id}?api_key={tmdb_api_key}'
    response = requests.get(tmdb_url)
    movie = {}
    if response.status_code == 200:
        movie = response.json()

    if request.method == 'POST':
        post_form = ForumPostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.movie = Movie.objects.get(tmdb_id=tmdb_id)
            post.author = request.user
            post.save()
            return redirect('movie_detail', tmdb_id=tmdb_id)
    else:
        post_form = ForumPostForm()

    return render(request, 'movies/movie_detail.html', {'movie': movie, 'post_form': post_form})
