from django.shortcuts import render
from django.conf import settings
from django.core.paginator import Paginator
import requests


def home(request):
    """
    View to render the home page and fetch the latest 18 entertainment articles from the News API.
    """
    api_key = settings.NEWS_API_KEY
    url = f'https://newsapi.org/v2/top-headlines?category=entertainment&pageSize=18&apiKey={api_key}'
    response = requests.get(url)
    articles = []

    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles', [])

    paginator = Paginator(articles, 6)  # Show 6 articles per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'home.html', {'page_obj': page_obj})

def movies(request):
    return render(request, 'movies/movies.html')


