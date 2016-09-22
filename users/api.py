# coding=utf-8
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_202_ACCEPTED, \
    HTTP_204_NO_CONTENT

from users.models import Profile
from users.permissions import UserPermission
from users.serializers import UserSerializer, BlogListSerializer


class UserSignUpAPI(APIView):
    """
    Endpoint de alta de usuario en POST
    """
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)



class UserDetailAPI (APIView):
    """
    Endpoint para obtener detalle GET con pk
    """
    permission_classes = (UserPermission,)
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=HTTP_200_OK)

    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        user.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class BlogListAPI (APIView):
    """
    Endpoint para obtener la lista de BLOGS a partir del username
    """
    def get(self, request):
        blogs = Profile.objects.all()
        serializer = BlogListSerializer(blogs, many=True)

        return Response(serializer.data)



