from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum_post_list, name='forum_post_list'),
    path('<int:id>/', views.forum_post_detail, name='forum_post_detail'),  # URL should include an integer value
]