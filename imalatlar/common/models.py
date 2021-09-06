from django.db import models

from ckeditor.fields import RichTextField

from .variables import DELIVERY_TYPES, COLORS, GLASS_TYPES, GLASS_TYPES_STANDART


class WorkOrderAbstractModel(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    crm = models.CharField('CRM NO', max_length=10)
    company_name = models.CharField(verbose_name='Firma', max_length=150)
    billing_address = models.CharField('Fatura Adresi', max_length=80)
    delivery_address = models.CharField('Sevk Adresi', max_length=80)
    delivery_date = models.DateField('Teslim Tarihi')
    created_time = models.DateTimeField('Olusturma Tarihi', auto_now_add=True)
    delivery_type = models.CharField('Teslim Sekli', choices=DELIVERY_TYPES, max_length=35)
    has_chest = models.BooleanField('Sandıklı Mı?')
    glass = models.CharField('Cam',choices=GLASS_TYPES, max_length=25, blank=True)
    color = models.CharField('Renk', max_length=27, choices=COLORS, blank=True)
    notes = RichTextField('Notlar', blank=True, null=True)
    drawing = models.CharField('Hazırlayan', max_length=200)
    control = models.CharField('Kontrol', blank=True, null=True, max_length=40)
    manufacturing_chief = models.CharField('Imalat Sorumlusu', blank=True, null=True, max_length=40)



    class Meta:
        abstract = True # ana bir modeldir database de gorunmez