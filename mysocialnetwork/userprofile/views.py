from rest_framework import generics
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from rest_framework.views import APIView

from .models import *
from .serializers import *


class UserAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


def pageNotFound(request, exception):
    return HttpResponseNotFound('Try to request another id')
