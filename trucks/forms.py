from django import forms
from .models import Trucks


class TrucksForm(forms.Form):
    truckgroup = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    shortname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    longname = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={"class": "form-control"}))
    truckinfo = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={"class": "form-control"}))
    storedplace = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class": "form-control"}))
    labelident = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class": "form-control"}))

