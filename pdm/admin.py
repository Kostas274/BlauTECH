from django.contrib import admin
from .models import Product, Group, Unit, Counterparty, ProductProperties, Spc

admin.site.register(Group)
admin.site.register(Unit)
admin.site.register(ProductProperties)

    
class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Main information', {'fields': [('part_number', 'partition'), ('name', 'group'), 'note']}),
        ('Production properties', {'fields': [('mass', 'cooperation'), ('cost', 'counterparty'), 'unit']}),
        ('Fail specification', {'fields': [('drawing', 'cam_file')]}),
    ]
    list_filter = ['partition']
    search_fields = ['name']   

admin.site.register(Product, ProductAdmin)


# class SpcInline(admin.TabularInline):
    # model = Spc

@admin.register(Spc)
class SpcAdmin(admin.ModelAdmin):
    list_display = ('owner', 'member', 'quantity')
    list_filter = ['owner']
    # inlines = [SpcInline]


class CounterpartyAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Main information', {'fields': [('name', 'property_form')]}),
        ('Adress information', {'fields': ['adress', ('email', 'site')]}),
        ('Phone numbers', {'fields': [('phone', 'viber')]}),
        ('Contact person', {'fields': [('l_name', 'm_name', 'f_name'), ('position', 'language'), 'last_visit']})
    ]
    list_filter = ['name']
    search_fields = ['name']

admin.site.register(Counterparty, CounterpartyAdmin)