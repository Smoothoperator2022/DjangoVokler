from django.db import models


# Create your models here. models = tables
class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)  # (means field could be free)

    def __str__(self):
        return self.name # to rename it in admin panel


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.PROTECT)

    def __str__(self): # to rename it in admin panel
        return f'Product: {self.name} | Category: {self.category.name}'
