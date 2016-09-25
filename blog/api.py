# coding=utf-8
from rest_framework import request
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly

from blog.models import BlogPost
from blog.serializers import PostListSerializer, PostSerializer
from blog.views import PostQuerySet, PostSearchQuerySet


class PostListAPI(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return PostQuerySet.get_posts_by_user(self.request.user)

    def get_serializer_class(self):
        return PostSerializer if self.request.method == 'POST' else PostListSerializer

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class PostListSearchAPI (ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        content = self.kwargs['title_content']
        return PostSearchQuerySet.get_posts_by_user_and_more(self, self.request, content)

    def get_serializer_class(self):
        return PostListSerializer if self.request.method == 'GET' else None


class PostDetailAPI (RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        return PostQuerySet.get_posts_by_user(self.request.user)

    def perform_update(self, serializer):
        return serializer.save(owner=self.request.user)
