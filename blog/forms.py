from django import forms
from .models import Post, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'author']

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']

template_name = "detail-list.html"