from django.shortcuts import render
from django.http import HttpResponse
from .models import Good, Category

def good_index(request, rubric = 0):
    categories = Category.objects.all()
     
    if rubric == 0:
        goods = Good.objects.none()
    else:
        goods = Good.objects.order_by('category', 'name').filter(category_id = rubric)
                
    return render(request, 'good_category.html', {'goods': goods, 'categories': categories})
