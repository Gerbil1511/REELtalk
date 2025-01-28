from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from movies.models import Movie
from forum.models import ForumPost

class TestMovieViews(TestCase):
    """
    Test cases for movie views.
    """

    def setUp(self):
        """
        Set up test data.
        """
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.movie = Movie.objects.create(
            tmdb_id=1,
            title='Test Movie',
            release_date='2023-01-01',
            poster_path='test_poster.jpg',
            overview='Test overview',
            popularity=10.0,
            vote_count=100,
            vote_average=8.0
        )
        self.forum_post = ForumPost.objects.create(
            movie=self.movie,
            author=self.user,
            title='Test Post',
            content='Test content',
            status=1
        )

    def test_list_movies_view(self):
        """
        Test the list_movies view.
        """
        response = self.client.get(reverse('list_movies'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movies/list_movies.html')

    def test_movie_detail_view(self):
        """
        Test the movie_detail view.
        """
        response = self.client.get(reverse('movie_detail', args=[self.movie.tmdb_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movies/movie_detail.html')

    def test_movie_detail_view_post(self):
        """
        Test the movie_detail view with a POST request.
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('movie_detail', args=[self.movie.tmdb_id]), {
            'title': 'New Post',
            'content': 'New content'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful post creation
        self.assertTrue(ForumPost.objects.filter(title='New Post').exists())