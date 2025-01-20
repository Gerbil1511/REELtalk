from django.shortcuts import render, get_object_or_404
from .models import ForumPost

def forum_post_list(request):
    posts = ForumPost.objects.all()
    return render(request, 'forum/forum_post_list.html', {'posts': posts})

def forum_post_detail(request, id):
    post = get_object_or_404(ForumPost, id=id)
    return render(request, 'forum/forum_post_detail.html', {'post': post})