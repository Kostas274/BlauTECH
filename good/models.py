from django.db import models
from datetime import date
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from pdm.models import Product


class Good(models.Model):
    good = models.OneToOneField("pdm.Product", null=True, on_delete=models.SET_NULL)
    name = models.CharField(_("name"), max_length=50, blank=False, unique=True)
    description = models.TextField(_("description"), blank=True)
    category = models.ForeignKey("Category", null=True, blank=False, on_delete=models.SET_NULL)
    price = models.DecimalField(_("price"), max_digits=8, decimal_places=2, blank=True)
    sale_start = models.DateField(_("sale_start"), blank=True, default=date.today)
    sale_end = models.DateField(_("sale_end"), null=True, blank=True) #, default=date.today)
    power = models.DecimalField(_("power"), max_digits=5, decimal_places=2, blank=True, default=0)
    productivity = models.DecimalField(_("productivity"), max_digits=5, decimal_places=2, blank=True, default=0)
    preview_qty = models.PositiveIntegerField(_("preview_qty"), blank=True, default=0)
    image = models.ImageField(upload_to='static/images', blank=True) #, height_field=None, width_field=None, max_length=100)
    
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
    
    def get_absolute_url(self):    
        return reverse('good_index', args=[self.pk])
    

    class Meta:
        ordering = ['name']        
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
