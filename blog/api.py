# coding=utf-8
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT

from blog.serializers import PostListSerializer, PostSerializer
from blog.views import PostQuerySet, PostSearchQuerySet


class PostListAPI(ListCreateAPIView):
    """
        Enpoint que devuelve un listado de Posts en función de las condiciones de usuario no autenticado (solo publicados),
         administrador autenticado (todos), usuario autenticado no administrador (los publicados de todos más los suyos
         aunque no estén publicados), ordenados por fecha de publicación y título.
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return PostQuerySet.get_posts_by_user(self.request.user)

    def get_serializer_class(self):
        return PostSerializer if self.request.method == 'POST' else PostListSerializer

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class PostListSearchAPI (ListAPIView):
    """
        Enpoint que devuelve un listado de Posts en función de un parámetro de búsqueda, que mira si forma parte de title
         o post_body del modelo BlogPost, siempre manteniendo las condiciones de usuario no autenticado (solo publicados),
         administrador autenticado (todos), usuario autenticado no administrador (los publicados de todos más los suyos
         aunque no estén publicados), ordenados por fecha de publicación y título.
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        content = self.kwargs['title_content']
        return PostSearchQuerySet.get_posts_by_user_and_more(self, self.request, content)

    def get_serializer_class(self):
        return PostListSerializer if self.request.method == 'GET' else None


class PostDetailAPI (RetrieveUpdateDestroyAPIView):
    """
        Enpoint que devuelve el detalle de un Post en función de las condiciones de usuario no autenticado (solo si publicado),
         administrador autenticado (todos), usuario autenticado no administrador (el suyo, publicado o no).
    """
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        return PostQuerySet.get_posts_by_user(self.request.user)

    def perform_update(self, serializer):
        return serializer.save(owner=self.request.user)


