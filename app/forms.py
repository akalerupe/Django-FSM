from django import forms
from django.forms.models import ModelForm
from app.models import Post

class PostForm(forms.ModelForm):
    class Meta:

        model = Post
        exclude = ('status',)
