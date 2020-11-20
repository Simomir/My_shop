from django.db import models


# class Product(models.Model):
#     name = models.CharField(max_length=60, blank=False, null=False)
#     user = models.ForeignKey(on_delete=models.CASCADE, related_name='products')
#     description = models.CharField(max_length=1500, blank=False)
#     image = models.ImageField(upload_to='shop/products/images')
#     price = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False)
#     available = models.BooleanField(default=True)
#
#     def __str__(self):
#         return f"{self.name}"
