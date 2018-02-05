from django.http import HttpResponse
from django import forms


def login(request):
    return HttpResponse('login: <input/> password: <input/>')
