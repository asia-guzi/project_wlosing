from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from project_wlosing import settings
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
# from .forms import WłosyForm





# Create your models here.




class Włosy(models.Model):
  
        DŁUGOŚĆ_CHOICES = [
            ("Krótkie", "Krótkie - do ramion"),
            ("Średnie", "Średnie - za ramiona"),
            ("Długie", "Długie - za łopatki"),
            ]

        KOLOR_CHOICES = [
            ("Blond", "Blond"),
            ("Szatynka", "Szatynka"),
            ("Brunetka", "Brunetka"),
            ("Rude", "Rude"),
            ]
        POROWATOŚĆ_CHOICES = [
            ("Wysokoporowate", "Wysokoporowate"),
            ("Średnioporowate", "Średnioporowate"),
            ("Niskoporowate", "Niskoporowate"),
            ]
        TYP_CHOICES = [
            ("Proste", "Proste - brak skrętu"),
            ("Falowane", "Falowane - typ 2a, 2b lub 2c"),
            ("Wurly", "Wurly - uzupełnij"),
            ("Kręcone", "Kręcone - typ 3a, 3b lub 3c"),
            ("Afro", "Afro - typ 4"),
            ]
        
        
        
        
        # input:
        # DŁUGOŚĆ_CHOICES = [
        #     "Krótkie",
        #     "Średnie",
        #     "Długie",
        #     ]

        # KOLOR_CHOICES = [
        #     "Blond",
        #     "Szatynka", 
        #     "Brunetka", 
        #     "Rude", 
        #     ]
        # POROWATOŚĆ_CHOICES = [
        #     "Wysokoporowate", 
        #     "Średnioporowate", 
        #     "Niskoporowate", 
        #     ]
        # TYP_CHOICES = [
        #     "Proste",
        #     "Falowane",
        #     "Wurly",
        #     "Kręcone",
        #     "Afro",
        #     ]
        
        # for x in DŁUGOŚĆ_CHOICES:
        #     for y in KOLOR_CHOICES:
        #         for z in POROWATOŚĆ_CHOICES:
        #             for q in TYP_CHOICES:
        #                 i = Włosy.objects.create()
        #                 i.set_all(x,y,z,q)
        #                 i.save()
        
        
        Długość = models.CharField(max_length=300, choices = DŁUGOŚĆ_CHOICES)
        Kolor = models.CharField(max_length=300, choices = KOLOR_CHOICES)
        Porowatość = models.CharField(max_length=100, choices = POROWATOŚĆ_CHOICES)
        Typ = models.CharField(max_length=300, choices = TYP_CHOICES)
        Owner=models.ManyToManyField(settings.AUTH_USER_MODEL,related_name="Typ_włosów", null=True, blank=True )
        

               
        def __str__(self):
            return f"Masz {self.Długość}, {self.Kolor}, {self.Porowatość}, {self.Typ} włosy. "
        
        def get_Długość(self):
            return self.Długość
        def get_Kolor(self):
            return self.Kolor
        def get_Porowatość(self):
            return self.Porowatość
        def get_Typ(self):
            return self.Typ
        
        def set_Długość(self, dlugosc):
             self.Długość = dlugosc
        def set_Kolor(self, kolor):
             self.Kolor = kolor
        def set_Porowatość(self, porowatosc):
             self.Porowatość = porowatosc
        def set_Typ(self, typ):
             self.Typ = typ
             
        def set_all(self, dlugosc, kolor, porowatosc, typ):
             self.set_Długość(dlugosc)
             self.set_Kolor(kolor)
             self.set_Porowatość(porowatosc)
             self.set_Typ(typ)
            
       
            
            
        
 
    
    
 


        
    
# class Porowatość (Włosy):

      
#       Właściwość = models.ForeignKey(Włosy, to_field="Porowatość", on_delete=models.CASCADE)

#       * = models.ForeignKey(Porowatość, related_name="Porowatość")
      
#       '''TBC - użyć jako foreignkey dla modelu Włosy |opis, hierarchia_PEH'''
        # """+ odnosniki do pielegnacji i odzywek"""
      
# class Typ (Włosy):
#     
#             * = models.ForeignKey(Typ, related_name="Typ")
              
#             """ jw + odnoniki do stylizacji"""

# class Rodzaj (Porowatość, Typ):
    
        
    
            
    
    
    
      
    