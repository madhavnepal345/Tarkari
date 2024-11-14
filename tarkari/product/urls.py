from django.urls import path
from . views import add_product,ad_product

urlpatterns=[ 
    path('add-product/',add_product,name='add_product'),
    path('ad-product/',ad_product,name='ad_product'),

]