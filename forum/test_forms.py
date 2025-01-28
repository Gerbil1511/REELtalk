from django.test import TestCase
from forum.forms import ForumPostForm, PostCommentForm

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