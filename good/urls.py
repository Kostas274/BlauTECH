from django.urls import path

from . import views

urlpatterns = [
    path('category/<int:category>', views.good_index, name='good_index'),
    path('category/<int:category>/create', views.good_create, name='good_create'),
#    path('good/<int:pk>/view', views.good_view, name='good_view'),
    path('good/<int:pk>/update', views.good_update, name='good_update'),
    path('good/<int:pk>/delete', views.good_delete, name='good_delete'),
]
