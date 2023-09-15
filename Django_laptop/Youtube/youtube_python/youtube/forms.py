from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(required = True,label='Username', max_length=20)
    password = forms.CharField(required = True,label='Password', max_length=20)

class RegisterForm(forms.Form):
    username = forms.CharField(required = True,label='Username', max_length=20)
    password = forms.CharField(required = True,label='Password', max_length=20)
    email = forms.EmailField(required = True,label='Email', max_length=40)
    age = forms.IntegerField(label='Age')
    #profilepic = forms.ImageField()

class CommentForm(forms.Form):
    text = forms.CharField(label='text', max_length=300)
    #video = forms.IntegerField(widget=forms.HiddenInput(), initial=1) 
    
class NewVideoForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    description = forms.CharField(label='Description', max_length=1000)
    file = forms.FileField(allow_empty_file=False)