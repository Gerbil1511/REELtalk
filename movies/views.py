from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Movie, Genre
import requests
from django.conf import settings
from .utils import fetch_movie_details, fetch_latest_news
from datetime import datetime

DEFAULT_POSTER_PATH = 'images/no_poster_for_movie.webp'  # Define the path to your default poster

def home(request):
    query = request.GET.get('q')
    movies = []
    if query:
        # Fetch movie data from TMDb API based on search query
        response = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={settings.TMDB_API_KEY}&query={query}')
        if response.status_code == 200:
            data = response.json()
            for item in data['results']:
                release_date_str = item.get('release_date')
                release_date = None
                if release_date_str:
                    try:
                        release_date = datetime.strptime(release_date_str, '%Y-%m-%d').date()
                    except ValueError:
                        release_date = None

                movie, created = Movie.objects.get_or_create(
                    tmdb_id=item['id'],
                    defaults={
                        'title': item['title'],
                        'overview': item['overview'],
                        'release_date': release_date,  # Set to None if missing or invalid
                        'poster_path': item.get('poster_path', DEFAULT_POSTER_PATH),  # Use default poster if missing
                        'vote_average': item['vote_average'],
                        'vote_count': item['vote_count']
                    }
                )
                if created:
                    # Associate genres with the movie
                    genre_ids = item['genre_ids']
                    for genre_id in genre_ids:
                        genre, _ = Genre.objects.get_or_create(tmdb_id=genre_id)
                        movie.genres.add(genre)
                movies.append(movie)
        else:
            messages.error(request, 'Failed to fetch movie data. Please try again later.')
    else:
        # Fetch top 20 latest movies from TMDb API
        response = requests.get(f'https://api.themoviedb.org/3/movie/now_playing?api_key={settings.TMDB_API_KEY}&language=en-US&page=1')
        if response.status_code == 200:
            data = response.json()
            for item in data['results']:
                release_date_str = item.get('release_date')
                release_date = None
                if release_date_str:
                    try:
                        release_date = datetime.strptime(release_date_str, '%Y-%m-%d').date()
                    except ValueError:
                        release_date = None

                movie, created = Movie.objects.get_or_create(
                    tmdb_id=item['id'],
                    defaults={
                        'title': item['title'],
                        'overview': item['overview'],
                        'release_date': release_date,  # Set to None if missing or invalid
                        'poster_path': item.get('poster_path', DEFAULT_POSTER_PATH),  # Use default poster if missing
                        'vote_average': item['vote_average'],
                        'vote_count': item['vote_count']
                    }
                )
                if created:
                    # Associate genres with the movie
                    genre_ids = item['genre_ids']
                    for genre_id in genre_ids:
                        genre, _ = Genre.objects.get_or_create(tmdb_id=genre_id)
                        movie.genres.add(genre)
                movies.append(movie)
        else:
            messages.error(request, 'Failed to fetch movie data. Please try again later.')

    # Fetch latest movie and entertainment news
    latest_news = fetch_latest_news()

    # Implement pagination for movies
    movie_paginator = Paginator(movies, 10)  # Show 10 movies per page
    movie_page_number = request.GET.get('page')
    movie_page_obj = movie_paginator.get_page(movie_page_number)

    # Implement pagination for news articles
    news_paginator = Paginator(latest_news, 4)  # Show 4 news articles per page
    news_page_number = request.GET.get('news_page')
    news_page_obj = news_paginator.get_page(news_page_number)

    return render(request, 'home.html', {
        'movie_page_obj': movie_page_obj,
        'news_page_obj': news_page_obj
    })

def movie_detail(request, tmdb_id):
    movie = get_object_or_404(Movie, tmdb_id=tmdb_id)
    movie_details = fetch_movie_details(movie.tmdb_id)
    forum_posts = movie.forum_posts.all()
    return render(request, 'movies/movie_detail.html', {'movie': movie, 'movie_details': movie_details, 'forum_posts': forum_posts})