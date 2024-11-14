from django.shortcuts import render
from .models import Product


def add_product(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        price=request.POST.get('price')
        description=request.POST.get('description')
        if title and price and description:
            if price.replace('.', '', 1).isdigit() and stock.isdigit():
                price=float(price)

                product.objects.create(
                    title=title,
                    price=price,
                    description=description,
                    category=category
                ) 
                return redirect (admin)
            else:
                return render("adminside/add_product.html",{'error':'price must be a valid number', 'categories': Product.CATEGORY_CHOICES})
        else:
            return render("adminside/add_product.html",{'error':'title,price and description are required','categories':Product.CATEGORY_CHOICES})

    return render(request, 'adminside/add_product.html',{'categories': Product.CATEGORY_CHOICES})

def ad_product(request):
    return render(request,'adminside/product.html')
