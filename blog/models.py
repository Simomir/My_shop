from django.db import models
from django.utils import timezone


class Post(models.Model):
    DRAFT = 'draft'
    PUBLISHED = 'published'
    choices = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='blog/posts/images')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=choices, default=DRAFT)

    class Meta:
        ordering = ['-publish']

    def __str__(self):
        return self.title
