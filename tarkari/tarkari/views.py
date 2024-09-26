from django.shortcuts import render
from product.models import *

def index(request):
    product_objects=Product.objects.all()
    data={
        'product_objects': product_objects

    }
    print(data)

    return render(request,'index.html',data)

def about(request):
    return render(request,'about.html')

