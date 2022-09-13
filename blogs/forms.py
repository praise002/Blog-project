from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import BlogPost


class BlogForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'text': 'Entry:'}
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80, 'rows': 20, 'style': 'resize: None;'}),
        }
        
        
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
