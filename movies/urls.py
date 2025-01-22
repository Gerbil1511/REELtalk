from django.urls import path
from . import views

urlpatterns = [
    path('', views.movies_list, name='movies_list'),
    path('movie/<int:tmdb_id>/', views.movie_detail, name='movie_detail'),
]