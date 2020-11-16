from django.shortcuts import render

from blog.models import Post


def index(request):
    return render(request, 'blog/index.html')


def post_detail(request):
    pass
