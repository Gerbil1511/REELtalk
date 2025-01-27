from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count, Q
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
            forum_post_list = ForumPost.objects.filter(title__icontains=search_query).annotate(comment_count=Count('comments'))
        else:
            forum_post_list = ForumPost.objects.filter(status=1).annotate(comment_count=Count('comments'))
        return forum_post_list
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['post_form'] = ForumPostForm()
    #     return context


def forum_post_detail(request, movie_slug, forum_post_slug):
    """
    View to display a single forum post and handle comment creation and editing.
    """
    movie = get_object_or_404(Movie, slug=movie_slug)
    forum_post = get_object_or_404(
        ForumPost, slug=forum_post_slug, movie=movie)

    if request.user.is_authenticated:
        comments = forum_post.comments.filter(Q(status=1) | Q(
            author=request.user)).order_by('-created_at')
        comment_count = forum_post.comments.filter(
            Q(status=1) | Q(author=request.user)).count()
    else:
        comments = forum_post.comments.filter(status=1).order_by('-created_at')
        comment_count = forum_post.comments.filter(status=1).count()

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
                messages.success(request, 'Your comment has been added and is awaiting approval.')
                return redirect('forum_post_detail', movie_slug=movie_slug, forum_post_slug=forum_post_slug)
    else:
        comment_form = PostCommentForm()

    return render(request, 'forum/forum_post_detail.html', {
        'forum_post': forum_post,
        'comments': comments,
        'comment_count': comment_count,
        'comment_form': comment_form,
        })


def comment_detail(request, movie_slug, forum_post_slug, comment_id):
    """
    View to display a single comment on a forum post.
    """
    movie = get_object_or_404(Movie, slug=movie_slug)
    forum_post = get_object_or_404(
        ForumPost, slug=forum_post_slug, movie=movie)
    comment = get_object_or_404(
        PostComment, id=comment_id, forum_post=forum_post, status=1)

    return render(request, 'forum/comment_detail.html', {
        'comment': comment,
    })


@login_required
def create_comment(request, movie_slug, forum_post_slug):
    """
    View to create a new comment. Only accessible to logged-in users.
    """
    movie = get_object_or_404(Movie, slug=movie_slug)
    forum_post = get_object_or_404(
        ForumPost, slug=forum_post_slug, movie=movie)

    if request.method == 'POST':
        comment_form = PostCommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.forum_post = forum_post
            comment.author = request.user
            comment.save()
            messages.success(
                request, 'Your comment has been added and is awaiting approval.')
            return redirect('forum_post_detail', movie_slug=movie_slug, forum_post_slug=forum_post_slug)
    else:
        comment_form = PostCommentForm()

    return render(request, 'forum/create_comment.html', {
        'comment_form': comment_form,
        'forum_post': forum_post,
    })


@login_required
def edit_comment(request, comment_id):
    """
    View to edit an existing comment. Only accessible to the comment's author.
    """
    comment = get_object_or_404(
        PostComment, id=comment_id, author=request.user)
    if request.method == 'POST':
        comment_form = PostCommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid():
            comment_form.save()
            messages.success(request, 'Your comment has been updated and is awaiting approval.')
            return redirect('forum_post_detail', movie_slug=comment.forum_post.movie.slug, forum_post_slug=comment.forum_post.slug)
    else:
        comment_form = PostCommentForm(instance=comment)

    return render(request, 'forum/edit_comment.html', {
        'comment_form': comment_form,
        'comment': comment,
    })


@login_required
def delete_comment(request, comment_id):
    """
    View to delete an existing comment. Only accessible to the comment's author.
    """
    comment = get_object_or_404(Comment, id=comment_id, author=request.user)
    post_slug = comment.post.slug
    movie_slug = comment.post.movie.slug
    if request.method == 'POST':
        comment.delete()
        messages.success(request, 'Your comment has been deleted.')
        return redirect('forum_post_detail', movie_slug=movie_slug, forum_post_slug=post_slug)

    return render(request, 'forum/delete_comment.html', {
        'comment': comment,
    })


@login_required
def upvote_post(request, post_id):
    """
    View to handle upvoting a forum post. Only accessible to logged-in users.
    """
    post = get_object_or_404(
        ForumPost, id=post_id)  # Get the post or return 404 if not found
    post.upvotes.add(request.user)  # Add the current user to the upvotes
    # Remove the current user from the downvotes
    post.downvotes.remove(request.user)
    return redirect('forum_post_list')  # Redirect to the forum post list


@login_required
def downvote_post(request, post_id):
    """
    View to handle downvoting a forum post. Only accessible to logged-in users.
    """
    post = get_object_or_404(
        ForumPost, id=post_id)  # Get the post or return 404 if not found
    post.downvotes.add(request.user)  # Add the current user to the downvotes
    # Remove the current user from the upvotes
    post.upvotes.remove(request.user)
    return redirect('forum_post_list')  # Redirect to the forum post list


@login_required
def create_post(request, movie_slug):
    """
    View to create a new forum post. Only accessible to logged-in users.
    """
    movie = get_object_or_404(Movie, slug=movie_slug)
    if request.method == 'POST':
        post_form = ForumPostForm(data=request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.movie = movie
            post.author = request.user
            post.save()
            messages.success(request, 'Your post has been created and is awaiting approval.')
            return redirect('forum_post_detail', movie_slug=movie.slug, forum_post_slug=post.slug)
    else:
        post_form = ForumPostForm()

    return render(request, 'forum/create_post.html', {
        'post_form': post_form,
        'movie': movie,
    })


@login_required
def edit_post(request, post_id):
    """
    View to edit an existing forum post. Only accessible to the post's author.
    """
    post = get_object_or_404(ForumPost, id=post_id, author=request.user)
    if request.method == 'POST':
        post_form = ForumPostForm(data=request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            messages.success(request, 'Your post has been updated and is awaiting approval.')
            return redirect('forum_post_detail', movie_slug=post.movie.slug, forum_post_slug=post.slug)
    else:
        post_form = ForumPostForm(instance=post)

    return render(request, 'forum/edit_post.html', {
        'post_form': post_form,
        'post': post,
    })


@login_required
def delete_post(request, post_id):
    """
    View to delete an existing forum post. Only accessible to the post's author.
    """
    post = get_object_or_404(ForumPost, id=post_id, author=request.user)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Your post has been deleted.')
        return redirect('forum_post_list')

    return render(request, 'forum/delete_post.html', {
        'post': post,
    })
