from django.db import models

class Trucks(models.Model):
    truckgroup = models.CharField(max_length=50, verbose_name='Камиони по групи')
    shortname = models.CharField(max_length=100, verbose_name='Късо име')
    longname = models.TextField(max_length=1000, verbose_name='Дълго име', blank='True')
    truckinfo = models.TextField(max_length=1000, verbose_name='Инфо за камиона')
    storedplace = models.CharField(max_length=150, verbose_name='Местодомуване')
    labelident = models.TextField(max_length=200, verbose_name='Етикет идентификация')

