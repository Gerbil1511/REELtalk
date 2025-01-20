from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def movies(request):
    return render(request, 'movies/movies.html')

def forum_post_list(request):
    return render(request, 'forum/forum_post_list.html')