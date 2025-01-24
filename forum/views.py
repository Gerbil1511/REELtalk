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
    searh_query = ForumPost.objects.filter(status=1)
    template_name = 'forum/forum_post_list.html'
    paginate_by = 10


def forum_post_detail(request, slug):
    """
    View to display a single forum post.
    """

    search_query = ForumPost.objects.filter(status=1)
    forum_post = get_object_or_404(search_query, slug=slug)
    comments = forum_post.comments.all().order_by('-created_at')
    comment_count = forum_post.comments.filter(approved_comment=True).count()


    if request.method == 'POST':
        comment_form = PostCommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = forum_post
            comment.author = request.user
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
                )

    comment_form = PostCommentForm()    
          

    return render(
        request, 'forum/forum_post_list.html',
        {
            'forum_post': forum_post,
            'comments': comments,
            'comment_form': comment_form,
            'comment_count': comment_count
         },
        )

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


# def forum_post_detail(request, id):
#     """
#     View to display the details of a single forum post, including comments.
#     Allows logged-in users to submit comments.
#     """
#     queryset = ForumPost.objects.filter(status=1)
#     post = get_object_or_404(ForumPost, id=id, status=1)  # Get the post or return 404 if not found
#     comments = forumpost.filter(approved_comment=True).order_by('-created_at')  # Get approved comments
#     comment_count = comments.count.filter(approved=True).count()

#     if request.method == 'POST':
#         # If the request method is POST, process the comment form
#         comment_form = PostCommentForm(data=request.POST)
#         if comment_form.is_valid():
#             # If the form is valid, save the comment but don't commit to the database yet
#             comment = comment_form.save(commit=False)
#             # Associate the comment with the post and the current user
#             comment.post = post
#             comment.author = request.user
#             # Save the comment to the database
#             comment.save()
#             messages.success(request, 'Comment submitted and awaiting approval')
#             # Redirect to the same post detail page
#             return redirect('forum_post_detail', id=post.id)
#     else:
#         # If the request method is GET, create an empty comment form
#         comment_form = PostCommentForm()

#     return render(request, 'forum/forum_post_detail.html', {
#         'post': post,
#         'comments': comments,
#         'comment_form': comment_form,
#         'comment_count': comment_count
#     })

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

# @login_required
# def edit_comment(request, comment_id):
#     """
#     View to edit a comment. Only accessible to the comment's author.
#     """
#     # Get the comment or return 404 if not found or if the user is not the author
#     comment = get_object_or_404(PostComment, id=comment_id, author=request.user)
    
#     if request.method == 'POST':
#         # If the request method is POST, process the comment form
#         comment_form = PostCommentForm(request.POST, instance=comment)
#         if comment_form.is_valid():
#             # If the form is valid, save the updated comment
#             comment_form.save()
#             messages.add_message(
#                 request, messages.SUCCESS,
#                 'Comment updated successfully'
#             )
#             # Redirect to the post detail page
#             return redirect('forum_post_detail', id=comment.post.id)
#     else:
#         # If the request method is GET, create a form with the existing comment data
#         comment_form = PostCommentForm(instance=comment)
    
#     # Render the edit comment template with the comment form
#     return render(request, 'forum/edit_comment.html', {'comment_form': comment_form})

# @login_required
# def delete_comment(request, comment_id):
#     """
#     View to delete a comment. Only accessible to the comment's author.
#     """
#     # Get the comment or return 404 if not found or if the user is not the author
#     comment = get_object_or_404(PostComment, id=comment_id, author=request.user)
#     post_id = comment.post.id  # Store the post ID to redirect after deletion
#     comment.delete()  # Delete the comment
#     messages.add_message(
#         request, messages.SUCCESS,
#         'Comment deleted successfully'
#     )
#     # Redirect to the post detail page
#     return redirect('forum_post_detail', id=post_id)

# def movie_detail(request, tmdb_id):
#     """
#     View to display the details of a single movie.
#     """
#     movie = get_object_or_404(Movie, tmdb_id=tmdb_id)  # Get the movie or return 404 if not found
#     return render(request, 'movies/movie_detail.html', {'movie': movie})
