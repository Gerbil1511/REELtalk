from django.shortcuts import render
from django.conf import settings
from django.core.paginator import Paginator
import requests


def home(request):
    """
    View to render the home page and fetch the latest 10 entertainment articles from the News API.
    """
    api_key = settings.NEWS_API_KEY
    url = f'https://newsapi.org/v2/top-headlines?category=entertainment&pageSize=10&apiKey={api_key}'
    response = requests.get(url)
    articles = []

    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles', [])

    paginator = Paginator(articles, 5)  # Show 5 articles per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'home.html', {'page_obj': page_obj})

def movies(request):
    return render(request, 'movies/movies.html')

def forum_post_list(request):
    return render(request, 'forum/forum_post_list.html')

