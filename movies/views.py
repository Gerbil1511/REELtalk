from django.shortcuts import render, get_object_or_404
from .models import Movie
from .utils import fetch_movie_details

# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    movie_details = fetch_movie_details(movie.tmdb_id)
    return render(request, 'movies/movie_detail.html', {'movie': movie, 'movie_details': movie_details})