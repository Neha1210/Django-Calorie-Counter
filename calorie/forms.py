from django.forms import ModelForm
from .models import*
from django import forms

class GetFoodinfoForm(ModelForm):
    class Meta:
        model=getfoodinfo
        fields=['food','cal']



