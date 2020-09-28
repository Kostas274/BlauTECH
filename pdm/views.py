from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def pdm_index(request, category = 0):

    if category == 0:
        products = Product.objects.none()
    else:
        partition_string = '1237'
        if partition_string.find(str(category)) > 0:
            products = Product.objects.order_by('partition', 'part_number').filter(partition = category)
        else:
            products = Product.objects.order_by('partition', 'name').filter(partition = category)
            
    return render(request, 'pdm_products.html', {'products': products})
