from django.shortcuts import render
from product.models import *

def index(request):
    product_objects=Product.objects.all()
    data={
        'product_objects': product_objects
    }
    return render(request,'index.html',data)

