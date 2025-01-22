from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Kategoriya nomi")

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey('product_app.Category', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.category.name}: {self.name}"
