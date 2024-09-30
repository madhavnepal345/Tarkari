from django.urls import path
from .views import about,PRODUCT,contact

urlpatterns = [

    path('about/',about,name='about'),
    path('product/',PRODUCT, name='productfrontend'),
    path('contact/',contact,name='contact'),
]

