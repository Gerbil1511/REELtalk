import requests
from django.conf import settings

def fetch_movie_details(movie_id):
    movie_url = f'https://api.themoviedb.org/3/movie/{movie_id}'
    credits_url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits'
    params = {
        'api_key': settings.TMDB_API_KEY,
        'language': 'en-US'
    }

    movie_response = requests.get(movie_url, params=params)
    credits_response = requests.get(credits_url, params=params)

    if movie_response.status_code == 200 and credits_response.status_code == 200:
        movie_data = movie_response.json()
        credits_data = credits_response.json()

        # Extract director information
        director = next((member['name'] for member in credits_data['crew'] if member['job'] == 'Director'), 'Unknown')

        # Extract main actors (e.g., top 3 actors)
        main_actors = ', '.join([actor['name'] for actor in credits_data['cast'][:3]])

        movie_data['director'] = director
        movie_data['main_actors'] = main_actors
        return movie_data
    else:
        return None  # Handle this case in your view