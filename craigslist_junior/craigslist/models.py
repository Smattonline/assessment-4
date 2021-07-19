from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    title = models.CharField(max_length=320, null=False)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=False, default=0)
    location = models.CharField(max_length=64, null=False)
    description = models.TextField(max_length=5000)
    
    def __str__(self):
        return f"{self.title} || ${self.price}" 