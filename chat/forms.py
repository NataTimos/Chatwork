from django import forms
from django.forms import fields
from .models import Post

class PostForm(forms.ModelForm):

    author = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Post
        fields = ('author', 'email', 'text',)


# class EmailPostForm(forms.Form):
#     name = forms.CharField(max_length=25)
#     email = forms.EmailField()
#     to = forms.EmailField()
#     comments = forms.CharField(required=False, widget=forms.Textarea)

