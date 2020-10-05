from django.urls import path

from . import views

urlpatterns = [
    path('partition/<int:category>/', views.product_list, name='product_list'),
    path('partition/<int:category>/create/', views.product_create, name='product_create'),
    path('product/<int:pk>/update/', views.product_update, name='product_update'),
    path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('product/<int:pk>/spc/', views.product_spc, name='product_spc'),


#    path('partition/<int:category>/', views.ProductListView.as_view(), name='product-list'),
#    path('product/<int:pk>/edit/', views.ProductUpdate.as_view(), name='product-edit'),   
#    path('product/<int:pk>/delete/', views.ProductDelete.as_view(), name='product-delete')
]
