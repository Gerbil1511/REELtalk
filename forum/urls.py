from django.urls import path
from . import views

urlpatterns = [
    path('', views.ForumPostList.as_view(), name='forum_post_list'),
    path('<slug:slug>/', views.forum_post_detail, name='forum_post_detail'), 
    path('post/<slug:slug>/upvote/', views.upvote_post, name='upvote_post'),
    path('post/<slug:slug>/downvote/', views.downvote_post, name='downvote_post'),
    # path('comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    # path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    # path('movie/<int:tmdb_id>/', views.movie_detail, name='movie_detail')
]