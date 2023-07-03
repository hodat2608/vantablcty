from django.forms import ModelForm
from .models import PostViews,CommentViews
from django import forms

class user_post_form(forms.ModelForm):
    class Meta:
        model = PostViews 
        fields = ['discription', 'post_image',]