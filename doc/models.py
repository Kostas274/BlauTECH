from django.db import models
from django.utils.translation import gettext_lazy as _


class Doc(models.Model):
    doc_number = models.CharField(_("doc_number"), max_length=30, db_index=True)
    name = models.CharField(_("name"), max_length=100, db_index=True)
    description = models.TextField(_("description"), blank=True)
    published_date= models.DateField(_("published_date"))
    image = models.ImageField(upload_to='certificates')
    
    def __str__(self):
        return (self.doc_number + " " + self.name)

    class Meta:
        ordering = ['name']
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

