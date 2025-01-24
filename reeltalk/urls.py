"""
URL configuration for reeltalk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import home, movies


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Home page view
    path('movies/', include('movies.urls')),  # Movies page view
    path('community/', include('forum.urls')),  # Include forum app URLs
    path('accounts/', include('allauth.urls')),  # Assuming you are using django-allauth for authentication
    path('summernote/', include('django_summernote.urls')),  # Include Summernote URLs
]