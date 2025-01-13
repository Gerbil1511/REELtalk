from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Movie, Genre
import requests
from django.conf import settings
from .utils import fetch_movie_details

def home(request):
    query = request.GET.get('q')
    movies = []
    if query:
        # Fetch movie data from TMDb API based on search query
        response = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={settings.TMDB_API_KEY}&query={query}')
        if response.status_code == 200:
            data = response.json()
            for item in data['results']:
                movie, created = Movie.objects.get_or_create(
                    tmdb_id=item['id'],
                    defaults={
                        'title': item['title'],
                        'overview': item['overview'],
                        'release_date': item['release_date'],
                        'poster_path': item['poster_path'],
                        'vote_average': item['vote_average'],
                        'vote_count': item['vote_count']
                    }
                )
                if created:
                    # Associate genres with the movie
                    genre_ids = item['genre_ids']
                    for genre_id in genre_ids:
                        genre = Genre.objects.get(tmdb_id=genre_id)
                        movie.genres.add(genre)
                movies.append(movie)
    else:
        # Fetch top 20 latest movies from TMDb API
        response = requests.get(f'https://api.themoviedb.org/3/movie/now_playing?api_key={settings.TMDB_API_KEY}&language=en-US&page=1')
        if response.status_code == 200:
            data = response.json()
            for item in data['results']:
                movie, created = Movie.objects.get_or_create(
                    tmdb_id=item['id'],
                    defaults={
                        'title': item['title'],
                        'overview': item['overview'],
                        'release_date': item['release_date'],
                        'poster_path': item['poster_path'],
                        'vote_average': item['vote_average'],
                        'vote_count': item['vote_count']
                    }
                )
                if created:
                    # Associate genres with the movie
                    genre_ids = item['genre_ids']
                    for genre_id in genre_ids:
                        genre = Genre.objects.get(tmdb_id=genre_id)
                        movie.genres.add(genre)
                movies.append(movie)
        else:
            messages.error(request, 'Failed to fetch movie data. Please try again later.')

    # Implement pagination
    paginator = Paginator(movies, 10)  # Show 10 movies per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'home.html', {'page_obj': page_obj})

def movie_detail(request, tmdb_id):
    movie = get_object_or_404(Movie, tmdb_id=tmdb_id)
    movie_details = fetch_movie_details(movie.tmdb_id)
    forum_posts = movie.forum_posts.all()
    return render(request, 'movies/movie_detail.html', {'movie': movie, 'movie_details': movie_details, 'forum_posts': forum_posts})