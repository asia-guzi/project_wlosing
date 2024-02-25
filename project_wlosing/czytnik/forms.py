# -*- coding: utf-8 -*-

from .models import Sklad
from django import forms

        
class SkladForm (forms.ModelForm):
    class Meta:
        model = Sklad
        fields = ["sklad_inci"]
