from django.db import models
from django.utils import timezone
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Post(models.Model):
    DRAFT = 'draft'
    PUBLISHED = 'published'

    choices = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
    )
    title = models.CharField(max_length=80, null=False, blank=False)
    slug = models.SlugField(max_length=100, unique_for_date='publish')
    body = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to=f'blog/posts/images')
    created = models.DateTimeField(auto_now_add=True, verbose_name='date created')
    updated = models.DateTimeField(auto_now=True, verbose_name='last updated')
    publish = models.DateTimeField(default=timezone.now, verbose_name='date published')
    status = models.CharField(max_length=10, choices=choices, default=DRAFT)

    class Meta:
        verbose_name = 'Blog post'
        verbose_name_plural = 'Blog posts'
        ordering = ['-publish']

    def __str__(self):
        return self.title


# Delete the image associated with the blog post on deletion of the post itself
@receiver(post_delete, sender=Post)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)
