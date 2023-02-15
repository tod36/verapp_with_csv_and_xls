from django.db import models

class Trucks(models.Model):
    truckgroup = models.CharField(max_length=50, verbose_name='Камиони по групи')
    shortname = models.CharField(max_length=100, verbose_name='Късо име')
    longname = models.TextField(max_length=1000, verbose_name='Дълго име', blank='True')
    truckinfo = models.TextField(max_length=1000, verbose_name='Инфо за камиона')
    storedplace = models.CharField(max_length=150, verbose_name='Местодомуване')
    labelident = models.TextField(max_length=200, verbose_name='Етикет идентификация')

    # def __str__(self):
    #     return self.truckgroup

    # class Meta:
    #     verbose_name = 'Камион'
    #     verbose_name_plural = 'Камиони'
    #     ordering = ['-storedplace']
# export to excel

# def highlight_cells(labelident):
#     color = '#65656' if labelident == 76 else '#kbkbkb'
#     # elif color = '#huhash' labelident == 77
#     return 'background-color: {}'.format(color)
#
# df.style.applymap(highlight_cells)

# def highlight_cells(labelident, color_if_true, color_if_false):
#     color = color_if_true if labelident == 76 else color_if_true
#     return 'background-color: {}'.format(color)
#
# df.style.applymap(highlight_cells, color_if_true='#hhjj', color_if_false='#RT465',
#                   subset=['sepal_length', 'petal_length'])