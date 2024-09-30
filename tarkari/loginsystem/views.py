from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Authenticating the user
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            # Log the user in and redirect to the homepage or dashboard
            login(request, user)
            return redirect('home')  # Replace 'home' with the appropriate URL name
        else:
            # If authentication fails, show an error message
            messages.error(request, 'Invalid email or password')
    
    return render(request, 'login.html')

