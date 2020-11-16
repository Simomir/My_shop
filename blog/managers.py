from django.db import models


class PublishedManager(models.Manager):
    """
    Custom manager to manipulate only published blog posts
    """
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')
