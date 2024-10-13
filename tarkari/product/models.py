from django.db import models

class Product(models.Model):
    title=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=5, decimal_places=2)
    description=models.TextField()
    image=models.ImageField(upload_to='media/')

    
    def __str__(self):
        return self.title

