from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Good, Category
# from pdm.models import Product

admin.site.register(Category)


class GoodAdmin(admin.ModelAdmin):
    fieldsets = [
        (_('Main information'), {'fields': [('name', 'category', 'good'), 'description']}),
        (_('Characterisitics'), {'fields': [('power', 'productivity')]}),
        (_('Trade information'), {'fields': [( 'sale_start', 'price', 'sale_end')]}),
        (_('Fail specification'), {'fields': [('image','preview_qty')]}),

    ]
    list_filter = ['category']
    search_fields = ['name']   

admin.site.register(Good, GoodAdmin)
