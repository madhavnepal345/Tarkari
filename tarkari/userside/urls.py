from django.urls import path
from .views import about,PRODUCT,submit_contact
from django.shortcuts import render

urlpatterns = [

    path('about/',about,name='about'),
    path('product/',PRODUCT, name='productfrontend'),
    path('contact/',submit_contact,name='contact'),
    path('thank-you/',lambda request: render(request,'thank_you.html'),name="thank_you"),
]

