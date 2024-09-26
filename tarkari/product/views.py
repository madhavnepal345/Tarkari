from django.shortcuts import render
from .models import Product


def product_views(request):
    
    return render(request,'products.html')
    product_objects=Product.objects.all()

