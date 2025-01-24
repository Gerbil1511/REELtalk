from django.urls import path
from . import views
from .views import ForumPostList, forum_post_detail, comment_detail 

urlpatterns = [
    path('', ForumPostList.as_view(), name='forum_post_list'),
    path('<slug:movie_slug>/<slug:forum_post_slug>/', forum_post_detail, name='forum_post_detail'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('post/<slug:slug>/upvote/', views.upvote_post, name='upvote_post'),
    path('post/<slug:slug>/downvote/', views.downvote_post, name='downvote_post'),
   
]