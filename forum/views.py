from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
from django.views import generic
from .models import ForumPost, PostComment
from movies.models import Movie
from .forms import PostCommentForm, ForumPostForm
import requests


class ForumPostList(generic.ListView):
    """
    View to list all forum posts. Allows searching by movie title.
    """
    model = ForumPost
    template_name = 'forum/forum_post_list.html'
    paginate_by = 10

    def get_queryset(self):
        search_query = self.request.GET.get('search', '')
        if search_query:
            forum_post_list = ForumPost.objects.filter(title__icontains=search_query)
        else:
            forum_post_list = ForumPost.objects.filter(status=1)
        return forum_post_list

def forum_post_detail(request, movie_slug, forum_post_slug):
    """
    View to display a single forum post and handle comment creation and editing.
    """
    movie = get_object_or_404(Movie, slug=movie_slug)
    forum_post = get_object_or_404(ForumPost, slug=forum_post_slug, movie=movie, status=1)
    comments = forum_post.comments.all().order_by('-created_at')
    comment_count = forum_post.comments.filter(approved_comment=True).count()

    if request.method == 'POST' and request.user.is_authenticated:
        if 'comment_id' in request.POST:
            # Editing an existing comment
            comment = get_object_or_404(PostComment, id=request.POST.get('comment_id'), author=request.user)
            comment_form = PostCommentForm(data=request.POST, instance=comment)
            if comment_form.is_valid():
                comment_form.save()
                messages.success(request, 'Your comment has been updated.')
                return redirect('forum_post_detail', movie_slug=movie_slug, forum_post_slug=forum_post_slug)
        else:
            # Creating a new comment
            comment_form = PostCommentForm(data=request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.forum_post = forum_post
                comment.author = request.user
                comment.save()
                messages.success(request, 'Your comment has been added.')
                return redirect('forum_post_detail', movie_slug=movie_slug, forum_post_slug=forum_post_slug)
    else:
        comment_form = PostCommentForm()

    return render(request, 'forum/forum_post_detail.html', {
        'forum_post': forum_post,
        'comments': comments,
        'comment_count': comment_count,
        'comment_form': comment_form,
    })

# def comment_detail(request, movie_slug, forum_post_slug, comment_id):
#     """
#     View to display a single comment on a forum post.
#     """
#     movie = get_object_or_404(Movie, slug=movie_slug)
#     forum_post = get_object_or_404(ForumPost, slug=forum_post_slug, movie=movie, status=1)
#     comment = get_object_or_404(PostComment, id=comment_id, forum_post=forum_post, approved_comment=True)

#     return render(request, 'forum/forum_post_detail.html', {
#         'comment': comment,
#     })

# @login_required
# def create_post(request):
#     """
#     View to create a new forum post. Only accessible to logged-in users.
#     """
#     if request.method == 'POST':
#         post_form = ForumPostForm(request.POST)
#         if post_form.is_valid():
#             post = post_form.save(commit=False)
#             post.author = request.user
#             post.save()
#             messages.add_message(
#                 request, messages.SUCCESS,
#                 'Post created successfully'
#             )
#             return redirect('forum_post_detail', id=post.id)
#     else:
#         post_form = ForumPostForm()

#     return render(request, 'forum/create_post.html', {'post_form': post_form})

# @login_required
# def edit_post(request, post_id):
#     """
#     View to edit a forum post. Only accessible to the post's author.
#     """
#     post = get_object_or_404(ForumPost, id=post_id, author=request.user)
    
#     if request.method == 'POST':
#         post_form = ForumPostForm(request.POST, instance=post)
#         if post_form.is_valid():
#             post_form.save()
#             messages.add_message(
#                 request, messages.SUCCESS,
#                 'Post updated successfully'
#             )
#             return redirect('forum_post_detail', id=post.id)
#     else:
#         post_form = ForumPostForm(instance=post)
    
#     return render(request, 'forum/edit_post.html', {'post_form': post_form})


# @login_required
# def delete_post(request, post_id):
#     """
#     View to delete a forum post. Only accessible to the post's author.
#     """
#     post = get_object_or_404(ForumPost, id=post_id, author=request.user)
#     post.delete()
#     messages.add_message(
#         request, messages.SUCCESS,
#         'Post deleted successfully'
#     )
#     return redirect('forum_post_list')

def comment_detail(request, movie_slug, forum_post_slug, comment_id):
    """
    View to display a single comment on a forum post.
    """
    movie = get_object_or_404(Movie, slug=movie_slug)
    forum_post = get_object_or_404(ForumPost, slug=forum_post_slug, movie=movie, status=1)
    comment = get_object_or_404(PostComment, id=comment_id, forum_post=forum_post, approved_comment=True)

    return render(request, 'forum/comment_detail.html', {
        'comment': comment,
    })


@login_required
def upvote_post(request, slug):
    """
    View to handle upvoting a forum post. Only accessible to logged-in users.
    """
    post = get_object_or_404(ForumPost, id=id)  # Get the post or return 404 if not found
    post.upvotes.add(request.user)  # Add the current user to the upvotes
    post.downvotes.remove(request.user)  # Remove the current user from the downvotes
    return redirect('forum_post_list')  # Redirect to the forum post list

@login_required
def downvote_post(request, slug):
    """
    View to handle downvoting a forum post. Only accessible to logged-in users.
    """
    post = get_object_or_404(ForumPost, id=id)  # Get the post or return 404 if not found
    post.downvotes.add(request.user)  # Add the current user to the downvotes
    post.upvotes.remove(request.user)  # Remove the current user from the upvotes
    return redirect('forum_post_list')  # Redirect to the forum post list


@login_required
def delete_comment(request, comment_id):
    """
    View to delete an existing comment. Only accessible to the comment's author.
    """
    # Get the comment or return 404 if not found or if the user is not the author
    comment = get_object_or_404(PostComment, id=comment_id, author=request.user)
    forum_post = comment.forum_post
    movie = forum_post.movie
    if request.method == 'POST':
        comment.delete()
        messages.success(request, 'Your comment has been deleted.')
        return redirect('forum_post_detail', movie_slug=movie.slug, forum_post_slug=forum_post.slug)

    return render(request, 'forum/delete_comment.html', {
        'comment': comment,
    })