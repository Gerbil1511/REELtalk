from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import ForumPost, PostComment

class ForumPostForm(forms.ModelForm):
    """
    Form for creating and editing ForumPost instances.

    Data is obtained from:
    - User input through the form fields.

    Data is returned as:
    - A ForumPost instance with the provided data.
    """
    class Meta:
        model = ForumPost
        fields = ['title', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10, 'cols': 80}),  # Replace Summernote widget with Textarea
        }


class PostCommentForm(forms.ModelForm):
    """
    Form for creating and editing PostComment instances.

    Data is obtained from:
    - User input through the form fields.

    Data is returned as:
    - A PostComment instance with the provided data.
    """
    class Meta:
        model = PostComment
        fields = ['comment']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5, 'cols': 80}),  # Replace Summernote widget with Textarea
        }