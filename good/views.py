from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.http import JsonResponse

from .models import Good, Category
from .forms import GoodForm

def good_index(request, category = 0):
    categories = Category.objects.all()    
    if category == 0:
        goods = Good.objects.none()
    else:
        goods = Good.objects.order_by('category', 'name').filter(category_id = category)
    return render(request, 'good/good_list.html', {'goods': goods, 'categories': categories})

def save_good_form(request, form, template_name, category):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            goods = Good.objects.all()
            data['html_good_list'] = render_to_string('good/partial_good_list.html', {'goods': goods, 'category': category})
        else:
            data['form_is_valid'] = False
    context = {'form': form, 'category': category}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def good_create(request, category):
    if request.method == 'POST':
        form = GoodForm(request.POST)
    else:
        form = GoodForm()
    return save_good_form(request, form, 'good/partial_good_create.html', category)

def good_update(request, pk):
    good = get_object_or_404(Good, pk=pk)
    if request.method == 'POST':
        form = GoodForm(request.POST, instance=good) 
    else:
        form = GoodForm(instance=good)
    return save_good_form(request, form, 'good/partial_good_update.html', good.category)
      
def good_delete(request, pk):
    good = get_object_or_404(Good, pk=pk)
    data = dict()
    if request.method == 'POST':
        good.delete()
        data['form_is_valid'] = True
        goods = Good.objects.all()
        data['html_good_list'] = render_to_string('good/good_list.html', {'goods': goods , 'category': good.category})
    else:
        context = {'good': good, 'category': good.category}
        data['html_form'] = render_to_string('good/partial_good_delete.html', context, request=request)
    return JsonResponse(data)