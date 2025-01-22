from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie
from forum.forms import ForumPostForm


def movies_list(request):
    """
    View to list movies based on search query.
    """
    search_query = request.GET.get('search', '')
    movie_results = []

    if search_query:
        movie_results = Movie.objects.filter(title__icontains=search_query)

    top_popular_movies = Movie.objects.order_by('-popularity')[:10]
    top_rated_movies = Movie.objects.order_by('-vote_average')[:10]

    return render(request, 'movies/movies_list.html', {
        'movie_results': movie_results,
        'search_query': search_query,
        'top_popular_movies': top_popular_movies,
        'top_rated_movies': top_rated_movies,
    })
  



def movie_detail(request, tmdb_id):
    """
    View to display the details of a single movie.
    Allows logged-in users to submit a post/review.
    """
    movie = get_object_or_404(Movie, tmdb_id=tmdb_id)
    
    if request.method == 'POST' and request.user.is_authenticated:
        post_form = ForumPostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.movie = movie
            post.author = request.user
            post.save()
            return redirect('forum_post_list')
    else:
        post_form = ForumPostForm() if request.user.is_authenticated else None

    return render(request, 'movies/movie_detail.html', {
        'movie': movie,
        'post_form': post_form,
    })