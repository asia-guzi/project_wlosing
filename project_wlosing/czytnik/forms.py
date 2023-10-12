# -*- coding: utf-8 -*-

from .models import Skład
from django import forms


        
class SkładForm (forms.ModelForm):
    class Meta:
        model = Skład
        fields = ["skład_INCI"]