from django.contrib import admin
from .models import Order, OrderItem

class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Main information', {'fields': [('order_number', 'order_date', 'counterparty')]}),
        ('Tax and discount', {'fields': ['amount', 'discount_percent', 'tax_percent', 'total']}),
        ('Fail specification', {'fields': ['image']})
    ]
    list_filter = ['counterparty', 'order_date']
    search_fields = ['counterparty']   

admin.site.register(Order, OrderAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'goods', 'quantity', 'price')
    list_filter = ['order']

admin.site.register(OrderItem, OrderItemAdmin)