from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, FormView
from .forms import EmailPostForm
from blog.models import Post
from django.core.mail import send_mail


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


class PostShareView(FormView):
    template_name = 'blog/post_share.html'
    form_class = EmailPostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = get_object_or_404(Post, id=self.kwargs['post_id'], status='published')
        context['post'] = post
        return context

    def form_valid(self, form):
        post = Post.objects.get(id=self.kwargs['post_id'])
        cd = form.cleaned_data
        post_url = self.request.build_absolute_uri(post.get_absolute_url())
        subject = f"{cd['name']} recommends you read {post.title}"
        message = f"Read {post.title} at {post_url}\n\n{cd['name']}\'s comments: {cd['comments']}"
        send_mail(subject, message, 'admin@myshop.com', [cd['to']])
        return render(self.request, 'blog/post_share.html', {'post': post, 'form': form, 'sent': True})

    def form_invalid(self, form):
        post = Post.objects.get(id=self.kwargs['post_id'])
        data = self.request.POST
        form = EmailPostForm(data=data)
        return render(self.request, 'blog/post_share.html', {'post': post, 'form': form, 'sent': False})
