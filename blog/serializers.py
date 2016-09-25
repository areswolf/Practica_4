# coding=utf-8
from rest_framework import serializers
from blog.models import BlogPost

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogPost



class PostListSerializer(PostSerializer):

    class Meta(PostSerializer.Meta):
        fields = ("title", "media_url", "introduction", "modified_at")





