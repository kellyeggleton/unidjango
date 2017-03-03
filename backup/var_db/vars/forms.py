from django import forms
from django.db import models
from .models import * 


class UploadFileForm(forms.Form):
    chromosome = forms.IntegerField()
    gene = forms.CharField()
    results = forms.FileField()


'''class Variant_DetailsSearchForm(forms.Form):
    keywords = forms.CharField(max_length=100)'''
