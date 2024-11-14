from django.db import models

# class Category(models.Model):
#     name=models.CharField(max_length=50)

#     def __str__(self):
#         return self.name
    

class Product(models.Model):
    CATEGORY_CHOICES=[
       ('fruits','Fruits'),
       ('vegetables','Vegetables')
    ]
    title=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=5, decimal_places=2)
    description=models.TextField()
    image=models.ImageField(upload_to='media/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)


    
    def __str__(self):
        return self.title

