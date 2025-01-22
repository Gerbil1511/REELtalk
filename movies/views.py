from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from .models import Movie
from .forms import ForumPostForm
import requests

def movies_list(request):
    # TMDB API search
    search_query = request.GET.get('search', '')
    tmdb_results = []
    if search_query:
        tmdb_api_key = settings.TMDB_API_KEY
        tmdb_url = f'https://api.themoviedb.org/3/search/movie?api_key={tmdb_api_key}&query={search_query}'
        response = requests.get(tmdb_url)
        if response.status_code == 200:
            tmdb_results = response.json().get('results', [])

    # Get the 10 most popular and top-rated movies
    popular_movies = Movie.objects.order_by('-popularity')[:10]
    top_rated_movies = Movie.objects.order_by('-vote_average')[:10]

    return render(request, 'movies/movies_list.html', {
        'tmdb_results': tmdb_results,
        'popular_movies': popular_movies,
        'top_rated_movies': top_rated_movies,
        
    })

def movie_detail(request, tmdb_id):
    tmdb_api_key = settings.TMDB_API_KEY
    tmdb_url = f'https://api.themoviedb.org/3/movie/{tmdb_id}?api_key={tmdb_api_key}'
    response = requests.get(tmdb_url)
    movie_data = {}
    if response.status_code == 200:
        movie_data = response.json()
        print("Fetched movie data:", movie_data)  # Debugging: Print fetched movie data

    # Ensure the Movie object exists in the database, if not, it will be created
    movie, created = Movie.objects.get_or_create(
        tmdb_id=tmdb_id,
        defaults={
            'poster_path': movie_data.get('poster_path', ''),
            'title': movie_data.get('title', ''),
            'slug': movie_data.get('slug', ''),
            'genre_ids': movie_data.get('genre_ids', []),
            'release_date': movie_data.get('release_date', ''),
            'overview': movie_data.get('overview', ''),
            'popularity': movie_data.get('popularity', 0),
            'vote_count': movie_data.get('vote_count', 0),
            'vote_average': movie_data.get('vote_average', 0),
        }
    )
    print("Movie object:", movie, "Created:", created)  # Debugging: Print movie object and creation status

    if request.method == 'POST':
        post_form = ForumPostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.movie = movie  # Use the movie object created or retrieved above
            post.author = request.user
            post.save()
            return redirect('movie_detail', tmdb_id=tmdb_id)
    else:
        post_form = ForumPostForm()

    return render(request, 'movies/movie_detail.html', {'movie': movie, 'post_form': post_form})