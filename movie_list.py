import os
import django
import requests

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reeltalk.settings')
django.setup()

from django.conf import settings
from movies.models import Movie

def fetch_and_populate_movies():
    tmdb_api_key = settings.TMDB_API_KEY
    popular_movies = []
    page = 1

    while len(popular_movies) < 200:
        tmdb_url = f'https://api.themoviedb.org/3/movie/popular?api_key={tmdb_api_key}&page={page}'
        response = requests.get(tmdb_url)
        if response.status_code != 200:
            break

        results = response.json().get('results', [])
        for movie in results:
            if len(popular_movies) >= 200:
                break

            movie_id = movie['id']
            movie_details_url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={tmdb_api_key}&append_to_response=release_dates'
            movie_details_response = requests.get(movie_details_url)
            if movie_details_response.status_code == 200:
                movie_details = movie_details_response.json()
                certifications = movie_details.get('release_dates', {}).get('results', [])
                for certification in certifications:
                    if certification['iso_3166_1'] == 'GB':  # Check for GB certification
                        for release_date in certification['release_dates']:
                            if release_date['certification'] in ['U', 'G', 'PG', 'PG-13', '0', '6', '12', '14', '12A', '15']:
                                popular_movies.append(movie_details)
                                break

        page += 1

    # Populate the Movie database
    for movie in popular_movies:
        Movie.objects.get_or_create(
            tmdb_id=movie['id'],
            defaults={
                'title': movie.get('title', ''),
                'poster_path': movie.get('poster_path', 'no_poster_for_movie.webp'),
                'release_date': movie.get('release_date', '1900-01-01'),
                'overview': movie.get('overview', 'No overview available'),
                'popularity': movie.get('popularity', 0.0),
                'vote_count': movie.get('vote_count', 0),
                'vote_average': movie.get('vote_average', 0.0),
                'genre_ids': movie.get('genre_ids', []),
            }
        )

if __name__ == "__main__":
    fetch_and_populate_movies()

    # Populate the Movie database
    for movie in popular_movies:
        poster_path = movie.get('poster_path', 'no_poster_for_movie.webp')
        if not poster_path:
            poster_path = 'no_poster_for_movie.webp'
        
        movie_obj, created = Movie.objects.get_or_create(
            tmdb_id=movie['id'],
            defaults={
                'title': movie.get('title', ''),
                'poster_path': poster_path,
                'release_date': movie.get('release_date', '1900-01-01'),
                'overview': movie.get('overview', 'No overview available'),
                'popularity': movie.get('popularity', 0.0),
                'vote_count': movie.get('vote_count', 0),
                'vote_average': movie.get('vote_average', 0.0),
                'genre_ids': movie.get('genre_ids', []),
            }
        )
        if not created:
            print(f"Skipped existing movie: {movie['title']} (TMDB ID: {movie['id']})")

if __name__ == "__main__":
    fetch_and_populate_movies()