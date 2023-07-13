from django.forms import ModelForm
from .models import PostViews,CommentViews,Repply_commentviews
from django import forms

class user_post_form(forms.ModelForm):
    class Meta:
        model = PostViews 
        fields = ['discription', 'post_image',]


class user_send_comment_form(forms.ModelForm):
    class Meta:
        model = CommentViews
        fields = ['message','massage_image',]

class repply_comment_form(forms.ModelForm):
    class Meta:
        model = Repply_commentviews
        fields = ['rep_message','rep_mess_image',]