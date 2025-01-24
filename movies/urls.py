from django.urls import path
from .views import movie_list, movie_detail

urlpatterns = [
    path('', movie_list, name='movies_list'),  # Use as_view() for class-based views
    path('movie/<int:tmdb_id>/', movie_detail, name='movie_detail'),  # import for function-based view
]