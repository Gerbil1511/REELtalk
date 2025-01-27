from django.urls import path
from . import views
from .views import ForumPostList, forum_post_detail, comment_detail 
from movies.views import movie_detail 

urlpatterns = [
    path('', views.ForumPostList.as_view(), name='forum_post_list'),
    path('post/create/', views.create_post, name='create_post'), 
    path('post/<int:post_id>/edit/', views.edit_post, name='edit_post'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
    path('post/<int:post_id>/upvote/', views.upvote_post, name='upvote_post'),
    path('post/<int:post_id>/downvote/', views.downvote_post, name='downvote_post'),
    path('post/<slug:movie_slug>/<slug:forum_post_slug>/', views.forum_post_detail, name='forum_post_detail'),
    path('comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('comment/<slug:movie_slug>/<slug:forum_post_slug>/<int:comment_id>/', views.comment_detail, name='comment_detail'),
    path('comment/<slug:movie_slug>/<slug:forum_post_slug>/create/', views.create_comment, name='create_comment'),
    path('movies/movie/<int:tmdb_id>/', movie_detail, name='movie_detail'),  # Ensure this line is correct
]
