from django.urls import path

from . import views

urlpatterns = [
    path('<int:category>/', views.pdm_index, name='pdm_index'),
]
