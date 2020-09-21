from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import date


class NullableCharField(models.CharField):
    description = "CharField that stores NULL but returns blank string"
   
    def to_python(self, value):
        if isinstance(value, models.CharField):
            return value 
        if value==None:
            return ""
        else:
            return value
      
    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return value or ''
        

class NullableEmailField(models.EmailField):
    description = "EmailField that stores NULL but returns blank string"
    
    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return value or ''
    
    def to_python(self, value):
        if isinstance(value, models.CharField):
            return value
        if value is None:
            return value
        return value or ''
        

class Product(models.Model):    
    FINISHED = 0
    COMPLEX = 1  
    ASSEMBLY = 2
    PART = 3
    STANDARD = 4
    BOUGHT = 5
    MATERIAL = 6
    SET = 7
    PARTITION_CHOICES = [
    	(FINISHED, 'Готовая продукция'),
        (COMPLEX, 'Комплексы'),
        (ASSEMBLY, 'Сборочные единицы'),
        (PART, 'Детали'),
        (STANDARD, 'Стандартные изделия'),
        (BOUGHT, 'Прочие изделия'),
        (MATERIAL, 'Материалы'),
        (SET, 'Комплекты'),
    ]
    partition = models.SmallIntegerField(choices=PARTITION_CHOICES, default=PART)
    part_number = NullableCharField(_("part_number"), max_length=50, null=True, blank=True, unique=True, default=None)
    name = models.CharField(_("name"), max_length=50, db_index=True, blank=False)        
    group = models.ForeignKey("Group", null=True, blank=True, on_delete=models.SET_NULL)
    note = models.CharField(_("note"), max_length=50, blank=True)   
    
    mass = models.DecimalField(_("mass"), max_digits=10, decimal_places=3, blank=True)
    unit = models.ForeignKey("Unit", null=True, blank=False, on_delete=models.SET_NULL)
    cost = models.DecimalField(_("cost"), max_digits=10, decimal_places=2, blank=True)      
    cooperation = models.BooleanField(_("cooperation"), default=False)
    counterparty = models.ForeignKey("Counterparty", null=True, blank=True, on_delete=models.SET_NULL)
    spc = models.ManyToManyField("self", symmetrical=False, through="Spc")
    
    drawing = models.FileField(upload_to='drawings', blank=True)
    cam_file = models.FileField(upload_to='cam_files', blank=True)
    
    def __str__(self):
        if self.partition > 3 and self.partition < 7:
            return self.name
        return (self.part_number + " " + self.name)

    class Meta:
        ordering = ['partition', 'part_number', 'name']
        verbose_name = 'ТМЦ'
        verbose_name_plural = 'ТМЦ'  
        
  
class Group(models.Model):
    name = models.CharField(_("name"), max_length=30, blank=False, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']        
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'  


class Unit(models.Model):
    name = models.CharField(_("name"), max_length=5, blank=False, unique=True)
    description = models.CharField(_("description"), max_length=30, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']              
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'
        

class Counterparty(models.Model):
    name = models.CharField(_("name"), max_length=50, blank=False, db_index=True)
    property_form = models.CharField(_("property_form"), max_length=5, blank=True)
#    email = models.EmailField(_('e-mail'), blank=True)
    email = NullableEmailField(_('e-mail'), blank=True, null=True, default=None, unique=True)
    site = models.URLField(blank=True)
    adress = models.CharField(_("adress"), max_length=50, blank=True)
    phone = models.CharField(_("phone"), max_length=15, blank=True)
    viber = models.CharField(_("viber"), max_length=15, blank=True)
    
    f_name = models.CharField(_("f_name"), max_length=15, blank=True)
    m_name = models.CharField(_("m_name"), max_length=15, blank=True)
    l_name = models.CharField(_("l_name"), max_length=15, blank=True)
    position = models.CharField(_("position"), max_length=20, blank=True)
    
    RU = "ru"  
    UA = "ua"
    PL = "pl"
    EN = "en"
    LANGUAGE_CHOICES = [
    	(RU, 'русский'),
        (UA, 'украинский'),
        (PL, 'польский'),
        (EN, 'английский'),
    ]
    language = models.CharField(_("language"), choices=LANGUAGE_CHOICES, default=RU, max_length=2)
    last_visit = models.DateField(_("last_visit"), default=date.today)  
    
    def __str__(self):
        return (self.name + ", " + self.property_form)

    class Meta:
        ordering = ['name']
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрагенты'
   
        
class Spc(models.Model):
    owner = models.ForeignKey("Product", blank=False, on_delete=models.CASCADE, related_name="holder")
    member = models.ForeignKey("Product", blank=False, on_delete=models.CASCADE, related_name="item")
    quantity = models.DecimalField(_("quantity"), max_digits=12, decimal_places=3, blank=False)
    
    # def __str__(self):
        # return (self.owner + ": " + self.member + ", " + str(self.quantity))
    
    class Meta:
        ordering = ['owner', 'member']        
        verbose_name = 'Спецификация'
        verbose_name_plural = 'Спецификации'
        
        
class ProductProperties(models.Model):
    prod = models.OneToOneField("Product", on_delete=models.CASCADE)       
    area = models.DecimalField(_("area"), max_digits=8, decimal_places=3, blank=True, default=0)
    coating = models.CharField(_("coating"), max_length=100, blank=True)
    treatment = models.CharField(_("treatment"), max_length=15, blank=True)
    stocksize = models.DecimalField(_("stocksize"), max_digits=10, decimal_places=3, blank=True, default=0)
    perimeter = models.DecimalField(_("perimeter"), max_digits=10, decimal_places=3, blank=True, default=0)
    incut = models.PositiveSmallIntegerField(_("incut"), blank=True, default=0)
    bend = models.PositiveSmallIntegerField(_("bend"), blank=True, default=0)
 
    def __str__(self):
        return (self.prod) 

    
    class Meta:
        ordering = ['prod']        
        verbose_name = 'Свойства деталей'
        verbose_name_plural = 'Свойства деталей'
