import os
import django
import requests
from django.utils.text import slugify

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reeltalk.settings')
django.setup()

from movies.models import Movie  # Import models after setting up Django

# TMDb API key
TMDB_API_KEY = os.environ.get('TMDB_API_KEY')


# Fetch top 25 top-rated movies from TMDb API
url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={TMDB_API_KEY}&language=en-US&page=1"
response = requests.get(url)

# Check if the request was successful
if response.status_code != 200:
    print(f"Failed to fetch data: {response.status_code}")
    exit()

data = response.json()

# Check if 'results' key is in the response JSON
if 'results' not in data:
    print("Key 'results' not found in the response JSON")
    exit()

# Number of movies to fetch
NUM_MOVIES = 25

for movie_data in data['results'][:NUM_MOVIES]:
    tmdb_id = movie_data['id']
    
    # Check if the movie already exists in the database
    if Movie.objects.filter(tmdb_id=tmdb_id).exists():
        print(f"Movie with TMDb ID {tmdb_id} already exists.")
        continue

    # Fetch movie details to get certifications
    details_url = f"https://api.themoviedb.org/3/movie/{tmdb_id}?api_key={TMDB_API_KEY}&append_to_response=release_dates"
    details_response = requests.get(details_url)
    details_data = details_response.json()
    
    # Check certifications
    certifications = details_data.get('release_dates', {}).get('results', [])
    exclude_movie = False
    for cert in certifications:
        if cert['iso_3166_1'] == 'US':
            for release_date in cert['release_dates']:
                if release_date['certification'] in ['18', 'R18']:
                    exclude_movie = True
                    break
        if exclude_movie:
            break
    
    if exclude_movie:
        print(f"Excluding movie with TMDb ID {tmdb_id} due to certification.")
        continue

    title = movie_data['title']
    overview = movie_data['overview']
    release_date = movie_data['release_date']
    poster_path = movie_data['poster_path']
    vote_average = movie_data['vote_average']
    vote_count = movie_data['vote_count']
    genre_ids = movie_data['genre_ids']

    # Generate slug from title and TMDb ID
    slug = slugify(f"{title}-{tmdb_id}")

    # Create and save the movie
    movie = Movie(
        title=title,
        slug=slug,
        tmdb_id=tmdb_id,
        overview=overview,
        release_date=release_date,
        poster_path=poster_path,
        vote_average=vote_average,
        vote_count=vote_count,
        genre_ids=genre_ids
    )
    movie.save()
    print(f"Added movie: {title}")