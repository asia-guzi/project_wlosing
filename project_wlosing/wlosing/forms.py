# -*- coding: utf-8 -*-
from django import forms

from .models import Włosy

class WłosyForm(forms.ModelForm):
    class Meta:
        model = Włosy
        fields = ["Długość", "Kolor", "Porowatość", "Typ"]
            
    