from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Movie
from forum.models import ForumPost
from forum.forms import ForumPostForm
from django.contrib import messages


def list_movies(request):
    """
    View to list all movies. Allows searching by movie title.

    Data is obtained from:
    - Movie model: Filters movies based on the search query.

    Data is returned as:
    - A rendered template with the list of movies and the search query.
    """
    search_query = request.GET.get('search', '')
    movie_list = None
    # If search query has data and is not empty, filter the
    # movies based on the query
    if search_query:
        # icontains is case-insensitive
        movie_list = Movie.objects.filter(title__icontains=search_query)
    context = {
        'movie_list': movie_list,
        'search_query': search_query,
        'latest_movies': Movie.objects.order_by('-release_date')[:10],
        'top_rated_movies': Movie.objects.order_by('-vote_average')[:10],
    }
    # Render the list_movies.html template with the context data
    return render(request, 'movies/list_movies.html', context)


def movie_detail(request, tmdb_id):
    """
    View to display details of a single movie and handle forum post creation.

    Data is obtained from:
    - Movie model: Retrieves the movie based on the TMDb ID.
    - ForumPost model: Retrieves forum posts associated with the movie.

    Data is returned as:
    - A rendered template with the movie details, post form, and user posts.
    """
    movie = get_object_or_404(Movie, tmdb_id=tmdb_id)
    user_posts = ForumPost.objects.filter(movie=movie, author=request.user) if request.user.is_authenticated else None

    if request.method == 'POST' and request.user.is_authenticated:
        post_form = ForumPostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.movie = movie
            post.author = request.user
            post.save()
            messages.success(request, 'Your post has been submitted and is awaiting approval.')
            return redirect('movie_detail', tmdb_id=tmdb_id)
    else:
        post_form = ForumPostForm() if request.user.is_authenticated else None

    return render(request, 'movies/movie_detail.html', {
        'movie': movie,
        'post_form': post_form,
        'user_posts': user_posts,
    })


@login_required
def edit_post(request, post_id):
    """
    View to edit an existing forum post. Only accessible to the post's author.

    Data is obtained from:
    - ForumPost model: Retrieves the forum post based on the post ID.

    Data is returned as:
    - A rendered template with the post form and post.
    """
    post = get_object_or_404(ForumPost, id=post_id, author=request.user)
    if request.method == 'POST':
        post_form = ForumPostForm(data=request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            messages.success(request, 'Your post has been updated.')
            return redirect('forum_post_detail', movie_slug=post.movie.slug, forum_post_slug=post.slug)
    else:
        post_form = ForumPostForm(instance=post)

    return render(request, 'movies/edit_post.html', {
        'post_form': post_form,
        'post': post,
    })


@login_required
def delete_post(request, post_id):
    """
    View to delete an existing forum post. Only accessible to post's author.

    Data is obtained from:
    - ForumPost model: Retrieves the forum post based on the post ID.

    Data is returned as:
    - A redirect to the forum post list page.
    """
    post = get_object_or_404(ForumPost, id=post_id, author=request.user)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Your post has been deleted.')
        return redirect('forum_post_detail', movie_slug=post.movie.slug, forum_post_slug=post.slug)

    return render(request, 'movies/delete_post.html', {
        'post': post,
    })