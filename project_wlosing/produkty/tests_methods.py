# -*- coding: utf-8 -*-

from produkty.models import *
from produkty.tests_function import ZmiennaUstalTest
import unittest as u


def view(r, m):
    print("----------------------------------------------------------------------")
    print(f"Testing method {r} of model {m}...")


def second():
    print(f"Error, test failed, this method does not work properly...")


def first():
    print(f"The test succided, this method works properly...")


class WorkingsKosmetykTest(u.TestCase):

    def test_set_work(self):
        view("set_work", "WorkingsKosmetyk")

        ZmiennaUstalTest.create_rodzaj()
        ZmiennaUstalTest.create_maski()
        ZmiennaUstalTest.create_oleje()
        ZmiennaUstalTest.create_szampony()

        outcome = {k.nazwa: f"kolejnosc = {k}, {k.nazwa}" for k in Kosmetyk.objects.all()}

        for name in outcome.keys():

            kolejnosc = Kosmetyk.objects.get(Nazwa=name)
            origin = WorkingsKosmetyk.set_work(kolejnosc)

            self.assertTrue(isinstance(origin, WorkingsKosmetyk))  # , second())
            self.assertEqual(origin.__str__(), outcome[name])  # , second())

        first()
        
        # pewnie jakie try bo mogą buć różnych długoci albo dodać zmienną i jeli nie t<=długoci krótzego słowa

    def test_check_b(self):
        view("check_b", "WorkingsKosmetyk")

        tuples = [("Mleko migdałowe", "Mleko owsiane"),
                  ("Orientalny ogród", "Orientalny zakątek"),
                  ("Kakao", "Kakaow"),
                  ("Kakao", "Kakaz"),
                  ("Kakao", "Kakaoa"),
                  ("Magnolia", "Mango")]
   
        f = True
        for x in tuples:
            name, nazwa = x
            test = WorkingsKosmetyk.check_b(name, nazwa)
            self.assertEqual(test, f)  # , second())
            
        ff = False
        for x in tuples:
            nazwa, name = x
            test = WorkingsKosmetyk.check_b(name, nazwa)
            self.assertEqual(test, ff)  # , second())
         
        first()

    def test_bisection(self):
           
        view("bisection", "WorkingsKosmetyk")

        ZmiennaUstalTest.create_rodzaj()
        ZmiennaUstalTest.create_maski()
        ZmiennaUstalTest.create_oleje()
        ZmiennaUstalTest.create_szampony()

        for x in Kosmetyk.objects.all():
            WorkingsKosmetyk.set_work(x)

        lista_wk = WorkingsKosmetyk.objects.all()

        outcomes = {n.nazwa: Kosmetyk.objects.get(Nazwa=n.nazwa) for n in lista_wk}

        for w in lista_wk:
            name_w = w.nazwa
            test = outcomes[name_w]

            origin = WorkingsKosmetyk.bisection(name_w, list(lista_wk))

            self.assertEqual(origin, test)  # , second())

        first()

    
    
   

    
   
