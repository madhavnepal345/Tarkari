from django.shortcuts import render
from .models import *
from .forms import *


def product_views(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
        
    return render(request,'products.html')
    product_objects=Product.objects.all()

