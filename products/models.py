from django.db import models
from users.models import User


class ProductCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='products_images', null=True, blank=True)
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'Product: {self.name} | Category: {self.category.name}'

    class Meta:
        ordering = ('id',)


class Rate(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    overview = models.CharField(max_length=100)
    rating = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.product} | Rate: {self.rating}'


class UserBookmarks(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Bookmarks for {self.user.username} | Product: {self.product.name}'
