from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from .models import Movie
from django.contrib.auth.decorators import login_required
from forum.models import ForumPost
from forum.forms import ForumPostForm


def movies_list(request):
    """
    View to list all movies. Allows searching by movie title.
    """
    search_query = request.GET.get('search', '')
    movie_results = []

    if search_query:
        movie_results = Movie.objects.filter(title__icontains=search_query)
    else:
        movie_results = Movie.objects.all()

    return render(request, 'movies/movies_list.html', {
        'movie_results': movie_results,
        'search_query': search_query,
    })

def movie_detail(request, tmdb_id):
    """
    View to display the details of a single movie.
    Allows logged-in users to submit a post/review.
    """
    movie = get_object_or_404(Movie, tmdb_id=tmdb_id)
    
    if request.method == 'POST':
        post_form = ForumPostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.movie = movie
            post.author = request.user
            post.save()
            return redirect('forum_post_list')
    else:
        post_form = ForumPostForm()

    return render(request, 'movies/movie_detail.html', {
        'movie': movie,
        'post_form': post_form,
    })