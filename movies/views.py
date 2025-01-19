from django.shortcuts import render, get_object_or_404
import requests
from django.conf import settings

def home(request):
    # Fetch top 20 movies from TMDb API
    tmdb_url = f'https://api.themoviedb.org/3/movie/now_playing?api_key={settings.TMDB_API_KEY}&language=en-US&page=1'
    tmdb_response = requests.get(tmdb_url)
    movies = tmdb_response.json().get('results', [])[:20]

    # Fetch latest entertainment news from News API
    news_url = f'https://newsapi.org/v2/top-headlines?category=entertainment&apiKey={settings.NEWS_API_KEY}'
    news_response = requests.get(news_url)
    news = news_response.json().get('articles', [])

    return render(request, 'home.html', {'movies': movies, 'news': news})

def movie_detail(request, movie_id):
    # Fetch movie details from TMDb API
    tmdb_url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={settings.TMDB_API_KEY}&language=en-US'
    tmdb_response = requests.get(tmdb_url)
    movie = tmdb_response.json()

    return render(request, 'movie_detail.html', {'movie': movie})