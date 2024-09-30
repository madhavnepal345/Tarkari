from django.shortcuts import render

def Admindashboard(request):
    return render(request, 'admin/index.html')