from django.shortcuts import render
from django.http import HttpResponse
from .models import Doc

def doc_index(request):
    """
    Function of displaying the documents page of the site.
    """
    docs = Doc.objects.order_by('name')
    return render(request, 'doc_index.html', {'docs': docs})
