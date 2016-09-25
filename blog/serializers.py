# coding=utf-8
from django.contrib.auth.models import User
from rest_framework import serializers
from blog.models import BlogPost
from blog.views import PostSearchQuerySet


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogPost



class PostListSerializer(PostSerializer):
    author = serializers.SerializerMethodField()

    class Meta(PostSerializer.Meta):
        fields = ("title", "author", "media_url", "introduction", "modified_at")


    def get_author(self, obj):
        return str(obj.owner.first_name) + " " + str(obj.owner.last_name)

