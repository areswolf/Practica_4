# coding=utf-8
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from blog.models import BlogPost


BADWORDS = ("meapilas", "aparcabicis", "tuercebotas", "abrazafarolas")
class PostForm(ModelForm):

    class Meta:
        model = BlogPost
        exclude = ['owner', 'post_likes']


    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get('description', '')
        for badword in BADWORDS:
            if badword in description:
                raise ValidationError("La palabra {0} no está permitida", format(badword))
        return cleaned_data
