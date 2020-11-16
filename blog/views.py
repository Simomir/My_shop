from django.shortcuts import render

from blog.models import Post


def index(request):
    posts = Post.published.all()
    return render(request, 'blog/index.html', {'posts': posts})


def post_detail(request):
    pass
