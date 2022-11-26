from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from .models import *


def getUser(request, userid):
    user = User.objects.filter(pk=userid)
    if user:
        return HttpResponse(user)
    return HttpResponseNotFound('There is no such user')


def pageNotFound(request, exception):
    return HttpResponseNotFound('Try to request another id')
