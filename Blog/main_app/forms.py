from django import forms
from .models import Post

class Form(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['Title', 'Content']