
from .models import *
from django import forms

# -*- coding: utf-8 -*-


class RdzForm(forms.Form):
    
    RODZAJ_CHOICES = [
        ("Szampon", "Szampon"),
        ("Odzywka", "Odzywka"),
        ("Maska", "Maska"),
        ("Olejek", "Olejek"),
        ("Olej", "Olej"),
        ("Wcierka", "Wcierka"),
        ("Zel", "Zel"),
        ("Pianka", "Pianka"),
        ("Krem", "Krem"),
        ("Peeling", "Peeling")]
    
    Rdz = forms.ChoiceField(choices=RODZAJ_CHOICES)
    
 
class SzamponForm (forms.ModelForm):
   
    class Meta:
        model = Szampon
        fields = ["marka", "nazwa", "moc", ]
      
        
class OdzywkaForm (forms.ModelForm):
    
    class Meta:
        model = Odzywka
        fields = ["marka", "nazwa", "PEH", ]
    
            
class MaskaForm (forms.ModelForm):

    class Meta:
        model = Maska
        fields = ["marka", "nazwa", "PEH", ]
        

class ZelForm (forms.ModelForm):

    class Meta:
        model = Zel
        fields = ["marka", "nazwa", "hold", ]
        

class PiankaForm (forms.ModelForm):

    class Meta:
        model = Pianka
        fields = ["marka", "nazwa", "hold", ]
        

class KremForm (forms.ModelForm):
    
    class Meta:
        model = Krem
        fields = ["marka", "nazwa", "hold", ]
        

class OlejekForm (forms.ModelForm):

    class Meta:
        model = Olejek
        fields = ["marka", "nazwa", ]
        

class OlejForm (forms.ModelForm):

    class Meta:
        model = Olej
        fields = ["marka", "nazwa", ]
        

class WcierkaForm (forms.ModelForm):

    class Meta:
        model = Wcierka
        fields = ["marka", "nazwa", ]
        

class PeelingForm (forms.ModelForm):

    class Meta:
        model = Peeling
        fields = ["marka", "nazwa", ]
