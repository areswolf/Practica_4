# coding=utf-8
from django.contrib.auth.models import User
from registration.forms import RegistrationForm
from django import forms


class ExRegistrationForm(RegistrationForm):
    username = forms.CharField(label="Usuario",max_length=25)
    first_name = forms.CharField(label="Nombre:", max_length=50)
    last_name = forms.CharField(label="Apellidos:", max_length=100)
    blog_title = forms.CharField(label="Título del blog", max_length=100)
    photo_url = forms.URLField(label="Foto de tu perfil")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'blog_title', 'photo_url')