from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .models import Trucks
from .forms import TrucksForm

import datetime as dt
import pandas as pd
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage

import csv


# def index(request):
#     trucks = Trucks.objects.all()
#     # result_truck = '<h1>List of trucks</h1>'
#     # for item in trucks:
#     #     result_truck += f'<div>\n<p>(item.truckgroup)</p>\n<p>(item.shortname)</p>\n</div>\n<hr>\n'
#     # return HttpResponse(result_truck)
#     # zamenqme gi sys sledva6tiq red
#     return render(request, 'trucks/index.html', {'trucks': trucks, 'title': 'List of trucks'})
# v sledva6tite redove kato dictionary

def index(request):
    trucks = Trucks.objects.all()
    context = {
        'trucks': trucks,
        'title': 'List of trucks'
    }
    return render(request, 'trucks/index.html', context)


# def proba(request):
#     return HttpResponse('<h2>Proba za drugi kamioni</h2>')
# mahame go i ot urls.py

# def add_trucks(request):
#     if request.method == 'POST':
#         form = TrucksForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             trucks = Trucks.objects.create(**form.cleaned_data)
#             # trucks = Trucks.objects.create(**form.cleaned_data)
#             return redirect(trucks)
#     else:
#         form = TrucksForm()
#     return render(request, 'trucks/add_trucks.html', {'form': form})

def exportexcel(request):
    if request.method == 'POST':
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="trucks.xls"'
        writer = csv.writer(response)
        # writer.writerow(['Trucks Detail'])

        writer.writerow(
            ['truckgroup', 'shortname', 'longname', 'truckinfo', 'storedplace', 'labelident'
             ])

        trucks = Trucks.objects.all().values_list('truckgroup', 'shortname', 'longname', 'truckinfo', 'storedplace',
                                                  'labelident'
                                                  )

        for truck in trucks:
            writer.writerow(truck)
        return response

    return render(request, 'trucks/exportexcel.html')
