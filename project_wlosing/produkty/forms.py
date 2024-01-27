from django import forms


from .models import *

# -*- coding: utf-8 -*-



class RdzForm(forms.Form):
    
    RODZAJ_CHOICES = [
    ("Szampon", "Szampon"), 
    ("Odżywka","Odżywka"), 
    ("Maska", "Maska"), 
    ("Olejek","Olejek"), 
    ("Olej","Olej"), 
    ("Wcierka","Wcierka"), 
    ("Żel","Żel"), 
    ("Pianka","Pianka"), 
    ("Krem","Krem"), 
    ("Peeling","Peeling")]
    
    Rdz = forms.ChoiceField(choices = RODZAJ_CHOICES)
    
 
class SzamponForm (forms.ModelForm):
   
    class Meta:
        model = Szampon
        fields = ["Marka", "Nazwa", "Moc", ]
      
        
class OdżywkaForm (forms.ModelForm):
    
    class Meta:
        model = Odżywka
        fields = ["Marka", "Nazwa", "PEH", ]
    
            
class MaskaForm (forms.ModelForm):

    class Meta:
        model = Maska
        fields = [ "Marka", "Nazwa", "PEH", ]
        
class ŻelForm (forms.ModelForm):

    class Meta:
        model = Żel
        fields = ["Marka", "Nazwa", "Hold", ]
        
class PiankaForm (forms.ModelForm):

    class Meta:
        model = Pianka
        fields = ["Marka", "Nazwa", "Hold", ]
        
class KremForm (forms.ModelForm):
    
    class Meta:
        model = Krem
        fields = [ "Marka", "Nazwa", "Hold", ]
        
class OlejekForm (forms.ModelForm):

    class Meta:
        model = Olejek
        fields = ["Marka", "Nazwa", ]
        
class OlejForm (forms.ModelForm):

    class Meta:
        model = Olej
        fields = ["Marka", "Nazwa", ]
        
class WcierkaForm (forms.ModelForm):

    class Meta:
        model = Wcierka
        fields = ["Marka", "Nazwa", ]
        
class PeelingForm (forms.ModelForm):

    class Meta:
        model = Peeling
        fields = ["Marka", "Nazwa", ]
        
        

        

        
    
        