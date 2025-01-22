from django.shortcuts import render
from .models import Movie

def movie_list(request):
    movies = Movie.objects.all()
    popular_movies = Movie.objects.order_by('-popularity')[:10]
    top_rated_movies = Movie.objects.order_by('-vote_average')[:10]
    return render(request, 'movies/movies.html', {
        'popular_movies': popular_movies,
        'top_rated_movies': top_rated_movies,
    })
  

def movie_detail(request, slug):
    movie = get_object_or_404(Movie, slug=slug)
    if request.method == 'POST':
        post_form = PostCommentForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.movie = movie
            post.author = request.user
            post.save()
            return redirect('movie_detail', slug=movie.slug)
    else:
        post_form = PostCommentForm()
    return render(request, 'movies/movie_detail.html', {
        'movie': movie,
        'post_form': post_form,
    })