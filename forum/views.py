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

    Data is obtained from:
    - ForumPost model: Filters and annotates forum posts based on search query and status.

    Data is returned as:
    - A queryset of forum posts with the count of published comments.
    """
    model = ForumPost
    template_name = 'forum/forum_post_list.html'
    paginate_by = 10

    def get_queryset(self):
        """
        Returns the filtered and annotated queryset of forum posts.
        """
        # Get the search query from the request
        search_query = self.request.GET.get('search', '')

        if search_query:
            # If there is a search query, filter forum posts by title containing the search query
            forum_post_list = ForumPost.objects.filter(
                title__icontains=search_query
            ).annotate(
                # Annotate each forum post with the count of comments that have status=1 (published)
                comment_count=Count('comments', filter=Q(comments__status=1))
            ).order_by('-created_at')  # Order the results by creation date in descending order
        else:
            # If there is no search query, filter forum posts by status=1 (published)
            forum_post_list = ForumPost.objects.filter(
                status=1
            ).annotate(
                # Annotate each forum post with the count of comments that have status=1 (published)
                comment_count=Count('comments', filter=Q(comments__status=1))
            ).order_by('-created_at')  # Order the results by creation date in descending order

        return forum_post_list  # Return the filtered and annotated queryset

def forum_post_detail(request, movie_slug, forum_post_slug):
    """
    View to display a single forum post and handle comment creation and editing.

    Data is obtained from:
    - Movie model: Retrieves the movie associated with the forum post.
    - ForumPost model: Retrieves the forum post based on the slug and movie.

    Data is returned as:
    - A rendered template with the forum post, comments, comment count, and comment form.
    """
    movie = get_object_or_404(Movie, slug=movie_slug)
    forum_post = get_object_or_404(ForumPost, slug=forum_post_slug, movie=movie)

    # Count published comments
    comment_count = forum_post.comments.filter(status=1).count()

    # Fetch comments for display
    if request.user.is_authenticated:
        comments = forum_post.comments.filter(Q(status=1) | Q(author=request.user)).order_by('-created_at')
    else:
        comments = forum_post.comments.filter(status=1).order_by('-created_at')

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

    return render(request, 'forum/forum_post_detail.html', {
        'comment': comment,
    })


@login_required
def create_comment(request, movie_slug, forum_post_slug):
    """
    View to create a new comment. Only accessible to logged-in users.

    Data is obtained from:
    - Movie model: Retrieves the movie associated with the forum post.
    - ForumPost model: Retrieves the forum post based on the slug and movie.

    Data is returned as:
    - A rendered template with the comment form and forum post.
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

    Data is obtained from:
    - PostComment model: Retrieves the comment based on the comment ID.

    Data is returned as:
    - A rendered template with the comment form and comment.
    """
    comment = get_object_or_404(PostComment, id=comment_id, author=request.user)
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

    Data is obtained from:
    - PostComment model: Retrieves the comment based on the comment ID.

    Data is returned as:
    - A rendered template with the comment.
    """
    comment = get_object_or_404(PostComment, id=comment_id, author=request.user)
    forum_post_slug = comment.forum_post.slug
    movie_slug = comment.forum_post.movie.slug
    if request.method == 'POST':
        comment.delete()
        messages.success(request, 'Your comment has been deleted.')
        return redirect('forum_post_detail', movie_slug=movie_slug, forum_post_slug=forum_post_slug)

    return render(request, 'forum/delete_comment.html', {
        'comment': comment,
        'forum_post_slug': forum_post_slug,
        'movie_slug': movie_slug,
    })


@login_required
def upvote_post(request, post_id):
    """
    View to upvote a forum post. Only accessible to logged-in users.

    Data is obtained from:
    - ForumPost model: Retrieves the forum post based on the post ID.

    Data is returned as:
    - A redirect to the forum post detail page.
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
    View to downvote a forum post. Only accessible to logged-in users.

    Data is obtained from:
    - ForumPost model: Retrieves the forum post based on the post ID.

    Data is returned as:
    - A redirect to the forum post detail page.
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

    Data is obtained from:
    - Movie model: Retrieves the movie associated with the forum post.

    Data is returned as:
    - A rendered template with the post form and movie.
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

    Data is obtained from:
    - ForumPost model: Retrieves the forum post based on the post ID.

    Data is returned as:
    - A rendered template with the post form and post.
    """
    post = get_object_or_404(ForumPost, id=post_id, author=request.user)
    if request.method == 'POST':
        post_form = ForumPostForm(data=request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            messages.success(request, 'Your post has been updated and is awaiting approval.')
            return redirect('forum_post_list')
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

    Data is obtained from:
    - ForumPost model: Retrieves the forum post based on the post ID.

    Data is returned as:
    - A rendered template with the post.
    """
    post = get_object_or_404(ForumPost, id=post_id, author=request.user)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Your post has been deleted.')
        return redirect('forum_post_list')

    return render(request, 'forum/delete_post.html', {
        'post': post,
    })
