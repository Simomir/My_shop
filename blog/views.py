from django.shortcuts import render, get_object_or_404

from blog.models import Post


def index(request):
    posts = Post.published.all()
    return render(request, 'blog/index.html', {'posts': posts})


def post_detail(request):
    pass
