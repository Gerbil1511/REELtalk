from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum_post_list, name='forum_post_list'),
    path('<int:id>/', views.forum_post_detail, name='forum_post_detail'),  # URL should include an integer value
    path('post/<int:id>/upvote/', views.upvote_post, name='upvote_post'),
    path('post/<int:id>/downvote/', views.downvote_post, name='downvote_post'),
    path('comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
]