# -*- coding: utf-8 -*-

from django.test import TestCase
from produkty.models import *
from produkty.tests_function import zmienna_ustalTest



def view(r,m):
    print("----------------------------------------------------------------------")
    print(f"Testing method {r} of model {m}...")
def second():
    print( f"Error, test failed, this method does not work properly...")
def first():
    print( f"The test succided, this method works properly...")




class workingsKosmetykTest(TestCase):
    
        
    def test_set_work(self):
        view("set_work", "workingsKosmetyk")
    
        zmienna_ustalTest.create_rodzaj(self)
        zmienna_ustalTest.create_maski(self)
        zmienna_ustalTest.create_oleje(self)
        zmienna_ustalTest.create_szampony(self)
        
        
        outcome = {(k.Nazwa): f"kolejnosc = {k}, {k.Nazwa}" for k in Kosmetyk.objects.all()}

        for name in outcome.keys():
            
            kolejnosc = Kosmetyk.objects.get(Nazwa=name)
            origin = workingsKosmetyk.set_work(kolejnosc)
        
            self.assertTrue(isinstance(origin, workingsKosmetyk))#, second())
            self.assertEqual(origin.__str__(), outcome[name]) #, second())
        
        first()
        
        # pewnie jakie try bo mogą buć różnych długoci albo dodać zmienną i jeli nie t<=długoci krótzego słowa
        
    def test_check_b(self):
        view("check_b", "workingsKosmetyk")
        
        
        tuples =  [("Mleko migdałowe", "Mleko owsiane"), 
                   ("Orientalny ogród", "Orientalny zakątek"),
                   ("Kakao", "Kakaow"),
                   ("Kakao", "Kakaz"),
                   ("Kakao", "Kakaoa"),
                   ("Magnolia", "Mango")]
   
        f=True
        for x in tuples:
            print(x)
            name, nazwa = x
            test = workingsKosmetyk.check_b(name, nazwa)
            print(test)
            self.assertEqual(test,f)#, second())
            
        ff=False
        for x in tuples:
            nazwa, name = x
            test = workingsKosmetyk.check_b(name, nazwa)
            self.assertEqual(test,ff)#, second())
         
        first()
        

    def test_bisection(self):
           
           view("bisection", "workingsKosmetyk")
           
           zmienna_ustalTest.create_rodzaj(self)
           zmienna_ustalTest.create_maski(self)
           zmienna_ustalTest.create_oleje(self)
           zmienna_ustalTest.create_szampony(self)

           for x in Kosmetyk.objects.all():
               workingsKosmetyk.set_work(x)
               
               
           lista_wK = workingsKosmetyk.objects.all()
           
           outcomes = {n.nazwa : Kosmetyk.objects.get(Nazwa = n.nazwa) for n in lista_wK}
         
           for w in lista_wK:
               name_w = w.nazwa
               test = outcomes[name_w]
               
               origin = workingsKosmetyk.bisection(name_w, list(lista_wK))
               
               self.assertEqual(origin,test)#, second())
               
           first() 
    
    
    
   

    
   
