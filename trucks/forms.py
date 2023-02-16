from .models import Trucks
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Row, Column, Field


class TrucksForm(forms.Form):
    truckgroup = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    shortname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    longname = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={"class": "form-control"}))
    truckinfo = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={"class": "form-control"}))
    storedplace = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class": "form-control"}))
    labelident = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class": "form-control"}))


class TrucksRegistration(forms.ModelForm):
    class Meta:
        model = Trucks
        fields = ['truckgroup', 'shortname', 'longname', 'truckinfo', 'storedplace', 'labelident'
                  ]
