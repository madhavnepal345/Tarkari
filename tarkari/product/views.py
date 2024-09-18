from django.shortcuts import render
from .models import product


def index(request):
    product_objects=product.objects.all()
    return render(request)

# Create your views here.
