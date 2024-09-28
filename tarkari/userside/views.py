from django.shortcuts import render
from product.models import Product


def about(request):
    return render (request,'about.html')

def PRODUCT(request):
    products_list=Product.objects.all()
    context = {'page_obj': products_list}
    print(context)
    return render(request,'products.html',context)


def contact(request):
    return render(request,'contact.html')
