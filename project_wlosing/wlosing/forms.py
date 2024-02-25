# -*- coding: utf-8 -*-
from django import forms

from .models import Wlosy


class WlosyForm(forms.ModelForm):
    class Meta:
        model = Wlosy
        fields = ["dlugosc", "kolor", "porowatosc", "typ"]
            
    