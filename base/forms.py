from django import forms
from agency.models import Post

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
