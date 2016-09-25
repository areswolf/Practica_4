# coding=utf-8
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from blog.models import BlogPost



class PostForm(ModelForm):

    class Meta:
        model = BlogPost
        exclude = ['owner', 'post_likes']


