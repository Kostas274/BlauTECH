from django.urls import path

from . import views

urlpatterns = [
    path('<int:rubric>/', views.good_index, name='good_index'),
]
