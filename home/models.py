from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='category/uploads', null='True')

    def __str__(self):
        return self.category

class Item(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name='item_category', on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='items/uploads', null='True')

    def __str__(self):
        return self.name