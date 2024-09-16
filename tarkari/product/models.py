from django.db import models

class Product(models.Model):
    title=models.CharField(max_length=50)
    Description=models.TextField(max_length=500)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    category=models.CharField(max_length=30)
    image=models.CharField(max_length=300)

    def __str__(self):
        return self.title