from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from product.models import *


def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user=authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Invalid email or password')
    return render(request,'login.html')


def register_view(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Check if the email is already taken
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered.')
        else:
            # Create the user
            user = User.objects.create_user(
                username=email,  # You can keep the email as the username
                email=email, 
                password=password, 
                first_name=first_name, 
                last_name=last_name
            )
            # Log the user in and redirect to the homepage
            login(request, user)
            return redirect('home')  # Replace 'home' with your homepage URL name
    
    return render(request, 'register.html')




@login_required
def index(request):
    product_objects=Product.objects.all()
    data={
        'product_objects': product_objects
    }
    return render(request,'index.html',data)
