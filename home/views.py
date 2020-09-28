from django.shortcuts import render

def home_index(request):
    """
    Function of displaying the home page of the site.
    """
    return render(request, 'home.html')