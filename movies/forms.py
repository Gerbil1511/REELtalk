from django import forms
from .models import ForumPost

class ForumPostForm(forms.ModelForm):
    """
    Form for creating and editing Movie instances.

    Data is obtained from:
    - User input through the form fields.

    Data is returned as:
    - A Movie instance with the provided data.
    """
    class Meta:
        model = ForumPost
        fields = ['title','content']