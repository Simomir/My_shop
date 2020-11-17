from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from blog.models import Post


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 6
    template_name = 'blog/index.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        year = self.kwargs['year']
        month = self.kwargs['month']
        day = self.kwargs['day']
        post = self.kwargs['post']
        return get_object_or_404(
            Post,
            slug=post,
            status='published',
            publish__year=year,
            publish__month=month,
            publish__day=day,
        )

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        return context
