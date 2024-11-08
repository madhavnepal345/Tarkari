from django.shortcuts import render

def dashboard(request):
    return render(request, 'adminside/index.html')

def ad_product(request):
    return render(request, 'adminside/add_product.html')