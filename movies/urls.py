from django.urls import path
from .views import list_movies, movie_detail
from . import views

urlpatterns = [
    path('', list_movies, name='list_movies'),  # Use as_view() for class-based views
    path('movie/<int:tmdb_id>/', movie_detail, name='movie_detail'),  # import for function-based view
]