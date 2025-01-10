from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('forum/<int:post_id>/', views.forum_post_detail, name='forum_post_detail'),
]

