import requests
from django.conf import settings

def fetch_movie_details(movie_id):
    """
    Fetches detailed information about a movie from The Movie Database (TMDb) API.

    Args:
        movie_id (int): The ID of the movie to fetch details for.

    Returns:
        dict: A dictionary containing movie details, including director and main actors.
        None: If the API request fails.

    Data is obtained from:
    - TMDb API endpoint for movie details: https://api.themoviedb.org/3/movie/{movie_id}
    - TMDb API endpoint for movie credits: https://api.themoviedb.org/3/movie/{movie_id}/credits

    Data is returned as a dictionary with additional keys:
    - 'director': The name of the movie's director.
    - 'main_actors': A comma-separated string of the top 3 main actors.
    """
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


def fetch_latest_news(page_size=20):
     """
    Fetches the latest news articles from a news API.

    Args:
        page_size (int): The number of news articles to fetch. Default is 20.

    Returns:
        dict: A dictionary containing the latest news articles.
        None: If the API request fails.

    Data is obtained from:
    - News API endpoint: https://newsapi.org/v2/top-headlines

    Data is returned as a dictionary containing the news articles.
    """
    api_key = settings.NEWS_API_KEY
    url = f'https://newsapi.org/v2/top-headlines?category=entertainment&pageSize={page_size}&apiKey={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        # Filter out articles with missing or removed titles
        filtered_articles = [article for article in articles if article.get('title') and article.get('title') != 'removed']
        return filtered_articles
    return []