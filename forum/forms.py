from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import ForumPost, PostComment

class ForumPostForm(forms.ModelForm):
     class Meta:
        model = ForumPost
        fields = ['title', 'content']
        widgets = {
            'content': SummernoteWidget(),
        }


class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ['comment']
        widgets = {
            'content': SummernoteWidget(),
        }