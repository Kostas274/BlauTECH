from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.http import JsonResponse

from .models import Product, Spc
from .forms import ProductForm

def product_list(request, category = 0):
    partition_string = '01237'
    if partition_string.find(str(category)) > 0:
        products = Product.objects.order_by('partition', 'part_number').filter(partition = category)
    else:
        products = Product.objects.order_by('partition', 'name').filter(partition = category)          
    return render(request, 'pdm/product_list.html', {'products': products, 'category': category})  

def save_product_form(request, form, template_name, category):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            products = Product.objects.all()
            data['html_product_list'] = render_to_string('pdm/partial_product_list.html', {'products': products, 'category': category})
        else:
            data['form_is_valid'] = False
    context = {'form': form, 'category': category}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
   
def product_create(request, category):
    if request.method == 'POST':
        form = ProductForm(request.POST)
    else:
        form = ProductForm()
    return save_product_form(request, form, 'pdm/partial_product_create.html', category)

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product) 
    else:
        form = ProductForm(instance=product)
    return save_product_form(request, form, 'pdm/partial_product_update.html', product.partition)
      
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    data = dict()
    if request.method == 'POST':
        product.delete()
        data['form_is_valid'] = True
        products = Product.objects.all()
        data['html_product_list'] = render_to_string('pdm/product_list.html', {'products': products , 'category': product.partition})
    else:
        context = {'product': product, 'category': product.partition}
        data['html_form'] = render_to_string('pdm/partial_product_delete.html', context, request=request)
    return JsonResponse(data)
    
def product_spc(request, pk):
    product = get_object_or_404(Product, pk=pk)
    spcs = Spc.objects.order_by('member__partition', 'member__part_number', 'member__name').filter(owner = pk)
    return render(request, 'pdm/product_spc.html', {'product': product, 'spcs': spcs})
