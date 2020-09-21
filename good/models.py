from django.db import models
from django.utils.translation import gettext_lazy as _
from pdm.models import Product


class Good(models.Model):
    name = models.CharField(_("name"), max_length=50, blank=False, unique=True)
    description = models.TextField(_("description"), blank=True)
    category = models.ForeignKey("Category", null=True, blank=False, on_delete=models.SET_NULL)
    good = models.OneToOneField("pdm.Product", null=True, on_delete=models.SET_NULL)   
    price = models.DecimalField(_("price"), max_digits=8, decimal_places=2, blank=True)
    production_date = models.DateField(_("production_date"), blank=True, auto_now_add=True)
    power = models.DecimalField(_("power"), max_digits=5, decimal_places=2, blank=True)
    productivity = models.DecimalField(_("productivity"), max_digits=5, decimal_places=2, blank=True)
    preview_qty = models.PositiveIntegerField(_("preview_qty"))
    image = models.ImageField(upload_to='goods') #, height_field=None, width_field=None, max_length=100)
    
    def __str__(self):
        return (self.name)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Товар'
        verbose_name = 'Товары'
        
        
class Category(models.Model):
    name = models.CharField(_("name"), max_length=30, blank=False, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']        
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
