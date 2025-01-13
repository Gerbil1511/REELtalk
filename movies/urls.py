from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movie/<slug:slug>/', views.movie_detail, name='movie_detail'), # Ensure this line captures the slug
]