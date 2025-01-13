from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Movie
from .utils import fetch_movie_details
import requests
from django.conf import settings
from django.utils.text import slugify

# Create your views here.

def home(request):
    query = request.GET.get('q')
    if query:
        # Fetch movie data from TMDb API
        response = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={settings.TMDB_API_KEY}&query={query}')
        data = response.json()
        movies = []
        for item in data['results']:
            movie, created = Movie.objects.get_or_create(
                tmdb_id=item['id'],
                defaults={
                    'title': item['title'],
                    'slug': slugify(item['title']),
                    'release_date': item['release_date'],
                    'poster_path': item['poster_path'],
                    'vote_average': item['vote_average'],
                    'vote_count': item['vote_count'],
                    'popularity': item['popularity'],
                    'genre_ids': ','.join(map(str, item['genre_ids']))
                }
            )
            if not created:
                    # Ensure the slug is unique if the movie already exists
                    movie.slug = slugify(item['title'])
                    unique_slug = movie.slug
                    num = 1
                    while Movie.objects.filter(slug=unique_slug).exists():
                        unique_slug = f'{movie.slug}-{num}'
                        num += 1
                    movie.slug = unique_slug
                    movie.save()
            movies.append(movie)
        else:
            movies = Movie.objects.none()
            messages.error(request, 'Failed to fetch movie data. Please try again later.')
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html', {'movies': movies})

def movie_detail(request, slug):  # Ensure this function accepts the slug parameter
    movie = get_object_or_404(Movie, slug=slug)  # Use slug to get the movie
    movie_details = fetch_movie_details(movie.tmdb_id)
    return render(request, 'movies/movie_detail.html', {'movie': movie, 'movie_details': movie_details})