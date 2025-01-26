from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import ForumPost, PostComment

class ForumPostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ['title', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10, 'cols': 80}),  # Replace Summernote widget with Textarea
        }


class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ['comment']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5, 'cols': 80}),  # Replace Summernote widget with Textarea
        }