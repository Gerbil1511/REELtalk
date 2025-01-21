
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import ForumPost 
from .forms import PostCommentForm

def forum_post_list(request):
    post_list = ForumPost.objects.all()
    paginator = Paginator(post_list, 10)  # Show 10 posts per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'forum/forum_post_list.html', {'page_obj': page_obj, 'is_paginated': page_obj.has_other_pages()})

def forum_post_detail(request, id):
    post = get_object_or_404(ForumPost, id=id)
    if request.method == 'POST':
        form = PostCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('forum_post_detail', post_id=post.id)
    else:
        form = PostCommentForm()
    return render(request, 'forum/forum_post_detail.html', {'post': post, 'form': form})