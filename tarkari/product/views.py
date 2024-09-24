from django.shortcuts import render
from .models import product


def index(request):
    product_objects=Product.objects.all()
    return render(request,'index.html')

# Create your views here.
