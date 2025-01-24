from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie
from forum.forms import ForumPostForm
from django.contrib import messages

def movie_list(request):
    """
    View to list movies based on various queries.
    """
    search_query = request.GET.get('search', '')
    if search_query:
        movie_list = Movie.objects.filter(title__icontains=search_query)
    else:
        movie_list = Movie.objects.all()

    context = {
        'movie_list': movie_list,
        'search_query': search_query,
        'latest_movies': Movie.objects.order_by('-release_date')[:10],  
        'top_rated_movies': Movie.objects.order_by('-vote_average')[:10],
    }

    return render(request, 'movies/movies_list.html', context)


def movie_detail(request, tmdb_id):
    """
    View to display the details of a single movie.
    Allows logged-in users to submit a post/review.
    """
    movie = get_object_or_404(Movie, tmdb_id=tmdb_id)
    
    if request.method == 'POST' and request.user.is_authenticated:
        post_form = ForumPostForm(data=request.POST)
        if post_form.is_valid():
            # If the form is valid, save the post but don't commit to the database yet
            post = post_form.save(commit=False)
            post.movie = movie
            post.author = request.user
            post.save()
            messages.add_message(
                request, messages.SUCCESS,
                    'Your post has been submitted and awaiting approval.'
            )
            return redirect('forum_post_list')   
    else:
        # If the request method is GET, create an empty post form if the user is authenticated
        post_form = ForumPostForm() if request.user.is_authenticated else None

        return render(
            request,
            'movies/movies_list.html', 
            {
                'movie': movie,
                'post_form': post_form,
            
            }
)