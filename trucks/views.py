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


def index(request):
    trucks = Trucks.objects.all()
    context = {
        'trucks': trucks,
        'title': 'List of trucks'
    }
    return render(request, 'trucks/index.html', context)


def exportexcel(request):
    if request.method == 'POST':
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="trucks.xls"'
        writer = csv.writer(response)

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
