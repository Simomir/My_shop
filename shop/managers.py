from django.db import models


class AvailableManager(models.Manager):
    """
    Custom manager to manipulate only available products
    """
    def get_queryset(self):
        return super(AvailableManager, self).get_queryset().filter(available=True)
