from django.conf import settings
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=60,
        blank=False,
        null=False
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='products'
    )

    description = models.CharField(
        _('Description'),
        max_length=1500,
        blank=False
    )

    image = models.ImageField(
        _('Image'),
        upload_to='shop/products/images',
        default='shop/products/no_image.jpeg',
    )

    price = models.DecimalField(
        _('Price'),
        max_digits=5,
        decimal_places=2,
        blank=False,
        null=False
    )

    available = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"


@receiver(post_delete, sender=Product)
def submission_delete(sender, instance, **kwargs):
    if 'products/images' in instance.image.url:
        instance.image.delete(False)
