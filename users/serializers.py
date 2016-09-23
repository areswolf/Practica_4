# coding=utf-8
from django.conf.urls import url
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from blog import urls
from sptBlogging.settings import BLOGS_URL
from users.models import Profile


class BlogListSerializer(serializers.Serializer):
    blog_title = serializers.CharField()
    blog_url = serializers.SerializerMethodField()

    class Meta:
        model = Profile

    def get_blog_url(self, obj):
        url = BLOGS_URL
        return url + str(obj.user)


class UserSerializer (serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.EmailField()

    def create(self, validated_data):
        instance = User()

        return self.update(instance, validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.password = make_password(validated_data.get('password'))
        instance.email = validated_data.get('email')

        instance.save()
        return instance




