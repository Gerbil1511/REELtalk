from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from forum.models import ForumPost, PostComment
from movies.models import Movie

class TestForumViews(TestCase):
    """
    Test cases for forum views.
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

    def test_forum_post_list_view(self):
        """
        Test the forum_post_list view.
        """
        response = self.client.get(reverse('forum_post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/forum_post_list.html')

    def test_forum_post_detail_view(self):
        """
        Test the forum_post_detail view.
        """
        response = self.client.get(reverse('forum_post_detail', args=[self.movie.slug, self.forum_post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/forum_post_detail.html')

    def test_create_post_view(self):
        """
        Test the create_post view.
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('create_post', args=[self.movie.slug]), {
            'title': 'New Post',
            'content': 'New content'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful post creation
        self.assertTrue(ForumPost.objects.filter(title='New Post').exists())

    def test_edit_post_view(self):
        """
        Test the edit_post view.
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('edit_post', args=[self.forum_post.id]), {
            'title': 'Updated Post',
            'content': 'Updated content'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful post update
        self.forum_post.refresh_from_db()
        self.assertEqual(self.forum_post.title, 'Updated Post')

    def test_delete_post_view(self):
        """
        Test the delete_post view.
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('delete_post', args=[self.forum_post.id]))
        self.assertEqual(response.status_code, 302)  # Redirect after successful post deletion
        self.assertFalse(ForumPost.objects.filter(id=self.forum_post.id).exists())