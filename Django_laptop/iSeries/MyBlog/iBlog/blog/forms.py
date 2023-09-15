from django import forms
from .models import Blog, Comment

class UploadForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('blog_title', 'blog_description')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']