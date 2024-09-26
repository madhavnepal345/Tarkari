from django import forms
from .models import *

class ProductForm(forms.modelforms):
    class Meta:
        model=Products
        fields="__all__"
