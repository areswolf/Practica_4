from django.contrib.auth.models import User
from django.db import models

from blog.validators import badwords

VISIBILITY_PUBLIC = 'PUB'
VISIBILITY_PRIVATE = 'PRI'

VISIBILITY = (
    (VISIBILITY_PUBLIC, 'Pública'),
    (VISIBILITY_PRIVATE, 'Privada')
)

STATUS_PUBLICATED = 'RDY'
STATUS_INPROGRES = 'INP'

STATUS = (
    (STATUS_PUBLICATED, 'Publicado'),
    (STATUS_INPROGRES, 'No publicado')
)


class Category(models.Model):
    category_name = models.CharField(max_length=50, null=False, default='General')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name

class BlogPost(models.Model):
    owner = models.ForeignKey(User, default=1)
    title = models.CharField(max_length=50, null=False, blank=False, default='Titulo', validators=[badwords])
    introduction = models.CharField(max_length=150, null=True, validators=[badwords])
    post_body = models.TextField(null=False, blank=False, default='Cuerpo del post', validators=[badwords])
    media_url = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    blog_category = models.ManyToManyField(Category)
    post_likes = models.CharField(max_length=10, null=False, default='0')
    visibility = models.CharField(max_length=3, choices=VISIBILITY, default=VISIBILITY_PUBLIC)
    status = models.CharField(max_length=3, choices=STATUS, default=STATUS_PUBLICATED)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ('created_at',)