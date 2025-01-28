from django.test import TestCase
from forum.forms import ForumPostForm, PostCommentForm
from forum.models import ForumPost
from movies.forms import MovieForm

class TestForumPostForm(TestCase):
    """
    Test cases for ForumPostForm.
    """

    def test_form_is_valid(self):
        """
        Test that the form is valid with correct data.
        """
        form_data = {'title': 'This is a great title', 'content': 'This is great content'}
        form = ForumPostForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_is_invalid_without_title(self):
        """
        Test that the form is invalid without a title.
        """
        form_data = {'content': 'This is great content'}
        form = ForumPostForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_form_is_invalid_without_content(self):
        """
        Test that the form is invalid without content.
        """
        form_data = {'title': 'This is a great title'}
        form = ForumPostForm(data=form_data)
        self.assertFalse(form.is_valid())

class TestPostCommentForm(TestCase):
    """
    Test cases for PostCommentForm.
    """

    def test_form_is_valid(self):
        """
        Test that the form is valid with correct data.
        """
        form_data = {'comment': 'This is a great comment'}
        form = PostCommentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_is_invalid_without_comment(self):
        """
        Test that the form is invalid without a comment.
        """
        form_data = {}
        form = PostCommentForm(data=form_data)
        self.assertFalse(form.is_valid())

class TestMovieForm(TestCase):
    """
    Test case for the MovieForm.
    """

    def test_form_is_valid(self):
        """
        Test that the form is valid with correct data.
        """
        form_data = {
            'title': 'Inception',
            'overview': 'A mind-bending thriller',
            'release_date': '2010-07-16',
            'poster_path': 'inception.jpg',
            'vote_average': 8.8,
            'vote_count': 20000,
            'popularity': 150.0,
            'genre_ids': [28, 12, 878]
        }
        movie_form = MovieForm(data=form_data)
        self.assertTrue(movie_form.is_valid())

    def test_form_is_invalid(self):
        """
        Test that the form is invalid with missing required fields.
        """
        form_data = {
            'title': '',
            'overview': '',
            'release_date': '',
            'poster_path': '',
            'vote_average': '',
            'vote_count': '',
            'popularity': '',
            'genre_ids': ''
        }
        movie_form = MovieForm(data=form_data)
        self.assertFalse(movie_form.is_valid())