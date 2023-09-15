from django import forms
from .models import post

choices = [('Technology', 'Technology'), ('Sports', 'Sports'), ('Entertainment', 'Entertainment'), ('Coding', 'Codings')]
class post_form(forms.ModelForm):
    class Meta:
        model = post
        fields = ('title', 'author', 'body', 'category')
        widget = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is a Blog Post'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is a Blog Post', 'id': 'author_create'}),
            #'author': forms.Select(attrs={'class': "form-control"}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choices)
        }

