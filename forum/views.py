
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import ForumPost, PostComment
from django.contrib import messages
from .forms import PostCommentForm

def forum_post_list(request):
    # Get all published forum posts
    post_list = ForumPost.objects.filter(status=1)
    paginator = Paginator(post_list, 10)  # Show 10 posts per page

    # Get the current page number from the request
    page_number = request.GET.get('page')
    # Get the page object for the current page
    page_obj = paginator.get_page(page_number)

    # Render the forum post list template with the page object and pagination status
    return render(request, 'forum/forum_post_list.html', {'page_obj': page_obj, 'is_paginated': page_obj.has_other_pages()})

def forum_post_detail(request, id):
    # Get the forum post with the given ID and status 1 (published)
    queryset = ForumPost.objects.filter(status=1)
    post = get_object_or_404(queryset, id=id)
    # Get all approved comments for the post, ordered by creation date
    comments = post.original_post.filter(approved_comment=True).order_by("-created_at")
    comment_count = comments.count()

    if request.method == 'POST':
        # If the request method is POST, process the comment form
        comment_form = PostCommentForm(data=request.POST)
        if comment_form.is_valid():
            # If the form is valid, save the comment but don't commit to the database yet
            comment = comment_form.save(commit=False)
            # Associate the comment with the post and the current user
            comment.original_post = post
            comment.comment_author = request.user
            # Save the comment to the database
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
            # Redirect to the same post detail page
            return redirect('forum_post_detail', post_id=post.id)
    else:
        # If the request method is GET, create an empty comment form
        comment_form = PostCommentForm()
    
    # Render the forum post detail template with the post, comments, comment form, and comment count
        return render(
        request,
        'forum/forum_post_detail.html',
        {
            'post': post,
            'comments': comments,
            'comment_form': comment_form,
            'comment_count': comment_count
        },
    )