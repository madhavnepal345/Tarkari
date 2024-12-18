from django.shortcuts import render,redirect
from product.models import Product
from .models import Contact
from django.contrib.auth.decorators import login_required



@login_required
def about(request):
    return render (request,'about.html')


@login_required
def PRODUCT(request):
    products_list=Product.objects.all()
    context = {'page_obj': products_list}
    print(context)
    return render(request,'products.html',context)

@login_required
def submit_contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')


        #validating all the forms
        if not name or not email or not subject or not message:
            error_message="All the fields are required"
            return render(request,'contact.html',{'error':error_message})
        
            # saving the data of the form into the database
        contact= Contact(name=name,email=email,subject=subject,message=message)
        
        contact.save()

        return redirect('thank_you')

    return render(request,'contact.html')


def cart(request):
    return render(request,'cart.html')
