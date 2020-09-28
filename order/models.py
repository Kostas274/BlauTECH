from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import date
from good.models import Good
from pdm.models import Counterparty


class Order(models.Model):
    order_number = models.CharField(_("order_number"), max_length=15, unique=True)
    order_date = models.DateField(_("order_date"), default=date.today)
    counterparty = models.ForeignKey("pdm.Counterparty", null=True, on_delete=models.SET_NULL)
    amount = models.DecimalField(_("amount"), max_digits=12, decimal_places=2, null=True, blank=True, default=0)
    discount_percent = models.DecimalField(_("discount_percent"), max_digits=5, decimal_places=2, blank=True, default=0)
    tax_percent = models.DecimalField(_("tax_percent"), max_digits=5, decimal_places=2, blank=True, default=0)
    total = models.DecimalField(_("total"), max_digits=12, decimal_places=2, blank=True, default=0)
    image = models.FileField(upload_to='order/image', blank=True)
    
    def __str__(self):
        return "#" + str(self.order_number) + "____" + str(self.counterparty) + "____" + str(self.total)

    class Meta:
        ordering = ['order_number']
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'
        

class OrderItem(models.Model):
    order = models.ForeignKey("Order", on_delete=models.CASCADE, null=False, blank=False)
    goods = models.ForeignKey("good.Good", on_delete=models.CASCADE, null=True, blank=False)
    quantity = models.DecimalField(_("quantity"), max_digits=12, decimal_places=3, null=False, blank=False)
    price = models.DecimalField(_("price"), max_digits=8, decimal_places=2, null=False, blank=False)

    
    class Meta:
        ordering = ['order']
        verbose_name = 'Состав счета'
        verbose_name_plural = 'Составы счетов'  
