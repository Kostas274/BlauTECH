from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import date
from good.models import Good
from pdm.models import Counterparty


class Order(models.Model):
    order_number = models.CharField(_("order_number"), max_length=15, unique=True)
    counterparty = models.ForeignKey("pdm.Counterparty", null=True, on_delete=models.SET_NULL)
    creation_date = models.DateField(_("creation_date"), default=date.today)
    amount = models.DecimalField(_("amount"), max_digits=12, decimal_places=2, blank=True)
    discount_percent = models.DecimalField(_("discount_percent"), max_digits=5, decimal_places=2, blank=True)
    tax_percent = models.DecimalField(_("tax_percent"), max_digits=5, decimal_places=2, blank=True)
    total = models.DecimalField(_("total"), max_digits=12, decimal_places=2, blank=True)
    image = models.FileField(upload_to='orders')
    # item = models.ManyToManyField("self", symmetrical=False, through="OrderItem")
    
    def __str__(self):
        return (self.order_number, self.counterparty, self.total)

    class Meta:
        ordering = ['order_number']
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'
        

class OrderItem(models.Model):
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    goods = models.ForeignKey("good.Good", on_delete=models.CASCADE)
    quantity = models.DecimalField(_("quantity"), max_digits=12, decimal_places=3, blank=False)
    price = models.DecimalField(_("price"), max_digits=8, decimal_places=2, blank=False)
    
    # def __str__(self):
        # return (self.order, self.goods, self.quantity)
    
    class Meta:
        ordering = ['order']
        verbose_name = 'Состав счета'
        verbose_name_plural = 'Составы счетов'
