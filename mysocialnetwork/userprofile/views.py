from rest_framework import generics
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from rest_framework.views import APIView

from .models import *
from .serializers import *


class UserAPIUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserAPICreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostAPIUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostAPICreate(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PointsAPIUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Points.objects.all()
    serializer_class = PointsSerializer


class PointsAPICreate(generics.CreateAPIView):
    queryset = Points.objects.all()
    serializer_class = PointsSerializer


class CommentsAPIUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class CommentsAPICreate(generics.CreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class PhotosAPIUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photos.objects.all()
    serializer_class = PhotosSerializer


class PhotosAPICreate(generics.CreateAPIView):
    queryset = Photos.objects.all()
    serializer_class = PhotosSerializer


def pageNotFound(request, exception):
    return HttpResponseNotFound('Try to request another id')
