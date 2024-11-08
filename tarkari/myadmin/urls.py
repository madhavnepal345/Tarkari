from django.urls import path
from . views  import dashboard,ad_product

urlpatterns = [
    path('admi/', dashboard, name='admin'),
    path('add-product/',ad_product,name='add_product'),

]
