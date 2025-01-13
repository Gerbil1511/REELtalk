from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import ForumPost
from .forms import ForumPostForm


def forum_post_list(request):
    posts = ForumPost.objects.all().order_by('-created_at')
    return render(request, 'forum/forum_post_list.html', {'posts': posts})


def forum_post_detail(request, post_id):
    post = get_object_or_404(ForumPost, id=post_id)
    if request.method == 'POST':
        if 'edit_post' in request.POST:
            if post.author == request.user:
                form = ForumPostForm(request.POST, instance=post)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Post updated successfully.')
                    return redirect('forum_post_detail', post_id=post.id)
            else:
                messages.error(request, 'You are not authorized to edit this post.')
        elif 'delete_post' in request.POST:
            if post.author == request.user:
                post.delete()
                messages.success(request, 'Post deleted successfully.')
                return redirect('forum_post_list')
            else:
                messages.error(request, 'You are not authorized to delete this post.')
    else:
        form = ForumPostForm(instance=post)
    return render(request, 'forum/forum_post_detail.html', {'post': post, 'form': form})


def create_or_edit_post(request, post_id=None):
    if post_id:
        post = get_object_or_404(ForumPost, id=post_id)
        if post.author != request.user:
            messages.error(request, 'You are not authorized to edit this post.')
            return redirect('forum_post_detail', post_id=post.id)
    else:
        post = None

    if request.method == 'POST':
        form = ForumPostForm(request.POST, instance=post)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            if post_id:
                messages.success(request, 'Post updated successfully.')
            else:
                messages.success(request, 'Post created successfully.')
            return redirect('forum_post_detail', post_id=new_post.id)
        else:
            messages.error(request, 'There was an error with your submission.')
    else:
        form = ForumPostForm(instance=post)

    return render(request, 'forum/forum_post_form.html', {'form': form})


def upvote_post(request, post_id):
    post = get_object_or_404(ForumPost, id=post_id)
    post.upvotes.add(request.user)
    messages.success(request, 'Post upvoted.')
    return redirect('forum_post_detail', post_id=post.id)


def downvote_post(request, post_id):
    post = get_object_or_404(ForumPost, id=post_id)
    post.downvotes.add(request.user)
    messages.success(request, 'Post downvoted.')
    return redirect('forum_post_detail', post_id=post.id)