from django import forms
from django.forms import ModelForm
from .models import Good


class GoodForm(ModelForm):  
    name = forms.CharField(required=True)
    description = forms.CharField(required=False)
    power = forms.DecimalField(max_digits=5, decimal_places=2, required=False)
    productivity = forms.DecimalField(max_digits=5, decimal_places=2, required=False)
    
    
    class Meta:
        model = Good
        fields = ('name', 'description', 'power', 'productivity')
