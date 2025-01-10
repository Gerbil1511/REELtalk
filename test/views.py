from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, ForumPost
from .forms import ForumPostForm


def home(request):
    query = request.GET.get('q')
    if query:
        movies = Movie.objects.filter(title__icontains=query)  # Add other filters as needed
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    posts = ForumPost.objects.filter(movie=movie)
    if request.method == 'POST':
        form = ForumPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.movie = movie
            post.author = request.user
            post.save()
            return redirect('forum_post_list', movie_id=movie.id)
    else:
        form = ForumPostForm()
    return render(request, 'forum_post_list.html', {'movie': movie, 'posts': posts, 'form': form})

def forum_post_detail(request, post_id):
    post = get_object_or_404(ForumPost, id=post_id)
    if request.method == 'POST':
        if 'edit_post' in request.POST:
            form = ForumPostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('forum_post_detail', post_id=post.id)
        elif 'delete_post' in request.POST:
            post.delete()
            return redirect('forum_post_list', movie_id=post.movie.id)
    else:
        form = ForumPostForm(instance=post)
    return render(request, 'forum_post_detail.html', {'post': post, 'form': form})

