from django import forms
from django.forms import ModelForm
from .models import Product


class ProductForm(ModelForm):  

    part_number = forms.CharField(required=False)
    name = forms.CharField(required=True)      
    note = forms.CharField(required=False) 

    
    class Meta:
        model = Product
        fields = ('part_number', 'name', 'note')
