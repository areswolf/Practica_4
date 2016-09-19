from django.contrib.auth.models import User
from django.db import models
from registration.signals import user_registered


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User)
    blog_title = models.CharField(max_length=100, blank=False, null=False, default='Titulo')
    photo_url = models.URLField(null=True, blank=True)
    num_of_posts = models.CharField(max_length=10, blank=False, null=False, default='0')
    num_of_likes = models.CharField(max_length=10, blank=False, null=False, default='0')

    def __unicode__(self):
        return self.user


def user_registered_callback(sender, user, request, **kwargs):
    profile = Profile(user=user)
    profile.blog_title = str(request.POST["blog_title"])
    profile.photo_url = str(request.POST["photo_url"])
    profile.save()


user_registered.connect(user_registered_callback)
