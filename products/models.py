from django.db import models
# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=254)
    author = models.CharField(max_length=254)
    tag = models.CharField(max_length=254)
    description = models.CharField(max_length=254, null=True, blank=True)
    content = models.CharField(max_length=254)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)

    def __str__(self):
        return self.title



