from django.urls import path
from . import views

urlpatterns = [
   path('', views.forum_post_list, name='forum_post_list'),
    path('post/<int:post_id>/', views.forum_post_detail, name='forum_post_detail'),
    path('post/<int:post_id>/upvote/', views.upvote_post, name='upvote_post'),
    path('post/<int:post_id>/downvote/', views.downvote_post, name='downvote_post'),
    path('post/new/', views.create_or_edit_post, name='create_post'),
    path('post/<int:post_id>/edit/', views.create_or_edit_post, name='edit_post'),
    path('post/<int:post_id>/delete/', views.create_or_edit_post, name='delete_post'),
]