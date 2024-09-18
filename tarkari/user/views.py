from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import message
from django.contrib import RegisterForm



def register(request):
    if request.method == 'POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            login(request,user)
            retrun redirect('auth_login')
        else:
            message.error(request,"Registration Failed.")
    else:
        from=RegisterForm()
    return render(request,'register.html',{'form':form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                message.error(request, "Invalid username or password.")
        else:
            message.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm(request)
    return render(request,'login.html',{'form':form})


@login_required
def welcome(request):
    return render(request,'welcome.html')

def logout_view(request):
    logout(request)
    return redirect('auth_login')