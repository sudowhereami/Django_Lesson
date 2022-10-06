from django.http import HttpResponse
from django.shortcuts import render
from . import models


def hello(request):
    return HttpResponse('<h1>Hello, World!</h1>')


def blog_all(request):
    post = models.Post.objects.all()
    return render(request, 'post_list.html', {'post': post})
