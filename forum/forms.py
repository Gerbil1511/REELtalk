from django import forms
from .models import ForumPost
from .models import PostComment

class ForumPostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ['title', 'content']


class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your comment here...'}),
        }