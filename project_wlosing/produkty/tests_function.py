
# -*- coding: utf-8 -*-

from produkty.views import wydziel, zmienna_ustal, ustal_form, obecnosc_ustal
from produkty.models import *
from produkty.forms import *

from django.test import TestCase

def view():
    print("----------------------------------------------------------------------")
    print("Testing function...")

class wydzielTest(TestCase):
   
    """
    Unit test for wydziel
    """
    
    def test_create_rodzaj(self):
        view()
        success=True
        # dictionary of pairs of words and outcomes to be returned
        words = {("Anwen, Proteinowa magnolia"): "Proteinowa magnolia",
                 ("OnlyBio, Odżywka emolientowa"): "Odżywka emolientowa",
                 ("Mleko owsiane"): "Mleko owsiane",
                 ("Taft, Curls"): "Curls",
                 ("Banfi"): "Banfi",}
                
        for word in words.keys():
            out = wydziel(word)
            if out != words[word]:
                print("FAILURE: test_wydziel()")
                print("\tExpected", words[word], " but got '" + \
                      out )
                success=False
        if  success:
            print("SUCCESS: test_wydziel()")
        self.assertTrue(success)     
        


class zmienna_ustalTest(TestCase):

    """
    Unit test for zmienna_ustal()
    """
    
    def create_rodzaj(self):
      
        
        for r in ["Szampon", "Odżywka", "Maska", "Olejek", "Olej", "Wcierka", "Żel", "Pianka", "Krem", "Peeling"]:
            Rdz.objects.create(Rodzaj=r)  
          
            
    def create_szampony(self):
        szampony = [
        ("Anwen","Mint it Up!", "Średni"),
        ]
        
  
        for s in szampony:
           x, y, z = s
           Szampon.objects.create(Marka=x, Nazwa=y, Moc=z)
            
    def create_maski(self):
        maski = [
           ("Garnier Hairfood", "Kakao", "Emolientowa"),
           ("Yope", "Mleko owsiane", "PEH"),
           ("Yope", "Orientalny ogród", "PEH"),
           ("Anwen", "Proteinowa magnolia", "Proteinowa"),
           ("OnlyBio", "Maska do włosów niskoporowatych", "PEH"),
           ]    
    
            
        for m in maski:
            x, y, z = m
            Maska.objects.create(Marka=x, Nazwa=y, PEH=z)
            
         
    def create_oleje(self):
        oleje = [
        ("OnlyBio", "Z pestek winogron"),
        ("Anwen", "Konopny")
        ]
       
        for o in oleje: 
            x,y = o
            Olej.objects.create(Marka=x, Nazwa=y)   
        
        
    def test_var_ustal(self):  
        view()
        

        success=True
        self.create_rodzaj()
        self.create_maski()
        self.create_oleje()
        self.create_szampony()
       
            
        #dict of inputs
        dictionary = {1:{}, 2:{"x":"z"}, 3:{"x":"z", "t": ["a","b"]} }
        
        # dict of expected outcomes
        sets = {1:{
                "Szampon": ["Anwen, Mint it Up!"], 
                "Maska":["Garnier Hairfood, Kakao", "Yope, Mleko owsiane", "Yope, Orientalny ogród", "Anwen, Proteinowa magnolia", "OnlyBio, Maska do włosów niskoporowatych"],
                "Olej":["OnlyBio, Z pestek winogron", 'Anwen, Konopny']
                },
            2:{"x" :"z",
                "Szampon": ["Anwen, Mint it Up!"], 
                "Maska":["Garnier Hairfood, Kakao", "Yope, Mleko owsiane", "Yope, Orientalny ogród", "Anwen, Proteinowa magnolia", "OnlyBio, Maska do włosów niskoporowatych"],
                "Olej":["OnlyBio, Z pestek winogron", 'Anwen, Konopny']
                },
            3:{"x" :"z",
               "t": ["a","b"],
                 "Szampon": ["Anwen, Mint it Up!"], 
                 "Maska":["Garnier Hairfood, Kakao", "Yope, Mleko owsiane", "Yope, Orientalny ogród", "Anwen, Proteinowa magnolia", "OnlyBio, Maska do włosów niskoporowatych"],
                 "Olej":["OnlyBio, Z pestek winogron", 'Anwen, Konopny']
                 }}
        
        for i in range(1,4) :
          
            d=dictionary[i]
            
            
            testowa = sets[i]
            
            zmienna = zmienna_ustal(d)
            
            
            for x in testowa.keys():
              
                try:
                    
                    if testowa[x] == zmienna[x]:
                       
                        pass
                    else:
                        success=False
                      
                        break
                except:
                    succes=False
                    break
                
     
   
        if success!=True:
                print("FAILURE: test_zmienna_ustal()")
                
        else :
                print("SUCCESS: test_zmienna_ustal()")
                
        print(success)
                
             
        self.assertTrue(success)        
            


        
class obecnosc_ustalTest(TestCase):
    
  
    
    def test_obecnosc_ustal(self):  
        view()
        
        zmienna_ustalTest.create_rodzaj(self)
        zmienna_ustalTest.create_maski(self)
        zmienna_ustalTest.create_oleje(self)
        zmienna_ustalTest.create_szampony(self)
    
     
        TR = {"Szampon": ["Anwen, Mint it Up!"], 
            "Maska":["Garnier Hairfood, Kakao", "Yope, Mleko owsiane", "Yope, Orientalny ogród", "Anwen, Proteinowa magnolia", "OnlyBio, Maska do włosów niskoporowatych"],
            "Olej":["OnlyBio, Z pestek winogron", 'Anwen, Konopny']}
        
        
        # ['Mint it Up!', "Kakao", "Mleko owsiane", "Orientalny ogród", "Proteinowa magnolia", "Maska do włosów niskoporowatych", "Z pestek winogron", 'Konopny']
        FA = {"Szampon" : "Anwen", 
              "Maska" : [], 
              "Olej" : ""} 
        
        f = True
        for x in TR.keys():
            for y in TR[x]:
                test = obecnosc_ustal(x, wydziel(y))
             
            self.assertEqual(f, test, f"for {x}, {y}")
            
        ff = False    
        for x in FA.keys():
            for y in FA[x]:
                test = obecnosc_ustal(x, y)
                self.assertEqual(ff, test, f"for {x}, {y}")
                
        print("SUCCESS: test_obecnosc_ustal()")
    
    
    # class ustal_formTest(TestCase):
        
    #     def test_form_ustal(self):  
            
    #         success=True
        
    #         rodzaje= ["Szampon", "Odżywka", "Maska", "Olejek", "Olej", "Wcierka", "Żel", "Pianka", "Krem", "Peeling"]
            
    #         formularze = [SzamponForm(),OdżywkaForm(), MaskaForm(), WcierkaForm(),PiankaForm(),ŻelForm(), KremForm(), PeelingForm(), OlejForm(), OlejekForm()]

        
    #         for r in rodzaje :
    #            form1 = formularze[rodzaje.index(r)]
               
    #            form2=ustal_form(r)
               
    #            if form1!=form2:
    #                success=False
              
    #            self.assertTrue(success)               
                





# # test_ustal_form()

