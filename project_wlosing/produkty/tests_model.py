from django.test import TestCase
from produkty.models import *


# Create your tests here.
def view(r):
    print("----------------------------------------------------------------------")
    print(f"Testing instance of {r} creation...")


def second(r):
    print(f"Error, the attempt to create an instance of {r} failed...")


class RdzTest(TestCase):

    @staticmethod
    def create_rdz(rodzaj="Olej"):
        return Rdz.objects.create(rodzaj=rodzaj)
        
    def test_rdz_creation(self):
        view("Rdz")
        w = self.create_rdz()
        self.assertTrue(isinstance(w, Rdz))  # , second("Rdz"))
        self.assertEqual(w.__str__(), w.rodzaj)  # , second("Rdz"))
                
                
class WorkingsKosmetykTest(TestCase):
    
    @staticmethod
    def create_kosmetyk(marka="Anwen", nazwa="Mint it up!"):
        return Kosmetyk.objects.create(marka=marka, nazwa=nazwa)
    
    @staticmethod
    def create_workingskosmetyk(kolejnosc, nazwa="Mint it up!"):
        return WorkingsKosmetyk.objects.create(kolejnosc=kolejnosc, nazwa=nazwa)
    
    def test_workings_creation(self):
        view("WorkingsKosmetyk")
        x = WorkingsKosmetykTest.create_kosmetyk()
        w = self.create_workingskosmetyk(x)

        self.assertTrue(isinstance(w, WorkingsKosmetyk))  # , second("WorkingsKosmetyk"))

        self.assertEqual(w.__str__(), f"kolejnosc = {w.kolejnosc}, {w.nazwa}")  # , second("WorkingsKosmetyk"))


class KosmetykTest(TestCase):

    @staticmethod
    def create_kosmetyk(marka, nazwa):
        return Kosmetyk.objects.create(marka=marka, nazwa=nazwa)
    
    def test_kosmetyk_creation(self):
        view("kosmetyk")
        w = KosmetykTest.create_kosmetyk(marka="Anwen", nazwa="Mint it up!")
        self.assertTrue(isinstance(w, Kosmetyk))  # , second("kosmetyk"))
        self.assertEqual(w.__str__(), f"{w.marka}, {w.nazwa} ")  # , second("kosmetyk"))


class SzamponTest(TestCase):

    @staticmethod
    def create_rdz(rodzaj="Szampon"):
        return Rdz.objects.create(rodzaj=rodzaj)
   
    @staticmethod
    def create_kosmetyk(marka="Anwen", nazwa="Mint it up!", moc="Średni"):
        return Szampon.objects.create(marka=marka, nazwa=nazwa, moc=moc)
    
    def test_kosmetyk_creation(self):
        view("Szampon")
        SzamponTest.create_rdz()
        w = self.create_kosmetyk()

        self.assertTrue(isinstance(w, Szampon))  # , second("Szampon"))
        self.assertEqual(w.__str__(), f"{w.marka}, {w.nazwa} ")  # , second("Szampon"))
            

class OdzywkaTest(TestCase):

    @staticmethod
    def create_rdz(rodzaj="Odzywka"):
        return Rdz.objects.create(rodzaj=rodzaj)
    
    @staticmethod
    def create_kosmetyk(marka="Anwen", nazwa="Proteinowa magnolia", PEH="Proteinowa"):
        return Odzywka.objects.create(marka=marka, nazwa=nazwa, PEH=PEH)
    
    def test_kosmetyk_creation(self):
        view("Odzywka")
        OdzywkaTest.create_rdz()
        w = OdzywkaTest.create_kosmetyk()
        self.assertTrue(isinstance(w, Odzywka))  # , second("Odzywka"))
        self.assertEqual(w.__str__(), f"{w.marka}, {w.nazwa} ")  # , second("Odzywka"))
            

class MaskaTest(TestCase):

    @staticmethod
    def create_rdz(rodzaj="Maska"):
        return Rdz.objects.create(rodzaj=rodzaj)

    @staticmethod
    def create_kosmetyk(marka="Garnier Hair Food", nazwa="Cocoa butter", PEH="Emolientowa"):
        return Maska.objects.create(marka=marka, nazwa=nazwa, PEH=PEH)
    
    def test_kosmetyk_creation(self):
        view("Maska")
        MaskaTest.create_rdz()
        w = MaskaTest.create_kosmetyk()
        self.assertTrue(isinstance(w, Maska))  # , second("Maska"))
        self.assertEqual(w.__str__(), f"{w.marka}, {w.nazwa} ")  # , second("Maska"))
            

class ZelTest(TestCase):

    @staticmethod
    def create_rdz(rodzaj="Zel"):
        return Rdz.objects.create(rodzaj=rodzaj)

    @staticmethod
    def create_kosmetyk(marka="Sysoss", nazwa="Power hold", hold="Mocny"):
        return Zel.objects.create(marka=marka, nazwa=nazwa, hold=hold)
    
    def test_kosmetyk_creation(self):
        view("Zel")
        ZelTest.create_rdz()
        w = ZelTest.create_kosmetyk()
        self.assertTrue(isinstance(w, Zel))  # , second("Zel"))
        self.assertEqual(w.__str__(), f"{w.marka}, {w.nazwa} ")  # , second("Zel"))
            

class PiankaTest(TestCase):

    @staticmethod
    def create_rdz(rodzaj="Pianka"):
        return Rdz.objects.create(rodzaj=rodzaj)

    @staticmethod
    def create_kosmetyk(marka="Wella", nazwa="Wellaflex", hold="Mocny"):
        return Pianka.objects.create(marka=marka, nazwa=nazwa, hold=hold)
    
    def test_kosmetyk_creation(self):
        view("Pianka")
        PiankaTest.create_rdz()
        w = PiankaTest.create_kosmetyk()
        self.assertTrue(isinstance(w, Pianka))  # , second("Pianka"))
        self.assertEqual(w.__str__(), f"{w.marka}, {w.nazwa} ")  # , second("Pianka"))
            

class KremTest(TestCase):

    @staticmethod
    def create_rdz(rodzaj="Krem"):
        return Rdz.objects.create(rodzaj=rodzaj)
        
    @staticmethod
    def create_kosmetyk(marka="Taft", nazwa="Curls", hold="Słaby"):
        return Krem.objects.create(marka=marka, nazwa=nazwa, hold=hold)
    
    def test_kosmetyk_creation(self):
        view("Krem")
        KremTest.create_rdz()
        w = KremTest.create_kosmetyk()
        self.assertTrue(isinstance(w, Krem))  # , second("Krem"))
        self.assertEqual(w.__str__(), f"{w.marka}, {w.nazwa} ")  # , second("Krem"))
            

class OlejekTest(TestCase):

    @staticmethod
    def create_rdz(rodzaj="Olejek"):
        return Rdz.objects.create(rodzaj=rodzaj)
        
    @staticmethod
    def create_kosmetyk(marka="Isana", nazwa="2in1 intensiv"):
        return Olejek.objects.create(marka=marka, nazwa=nazwa)
    
    def test_kosmetyk_creation(self):
        view("Olejek")
        OlejekTest.create_rdz()
        w = OlejekTest.create_kosmetyk()
        self.assertTrue(isinstance(w, Olejek))  # , second("Olejek"))
        self.assertEqual(w.__str__(), f"{w.marka}, {w.nazwa} ")  # , second("Olejek"))
            

class OlejTest(TestCase):

    @staticmethod
    def create_rdz(rodzaj="Olej"):
        return Rdz.objects.create(rodzaj=rodzaj)
       
    @staticmethod
    def create_kosmetyk(marka="OnlyBio - Hair in balance", nazwa="Olej do olejowania do włosów wysokoporowatych"):
        return Olej.objects.create(marka=marka, nazwa=nazwa)
    
    def test_kosmetyk_creation(self):
        view("Olej")
        OlejTest.create_rdz()
        w = OlejTest.create_kosmetyk()
        self.assertTrue(isinstance(w, Olej))  # , second("Olej"))
        self.assertEqual(w.__str__(), f"{w.marka}, {w.nazwa} ")  # , second("Olej"))
            

class WcierkaTest(TestCase):
    
    @staticmethod
    def create_rdz(rodzaj="Wcierka"):
        return Rdz.objects.create(rodzaj=rodzaj)
    
    @staticmethod
    def create_kosmetyk(marka="Anwen", nazwa="Grow Us Tender"):
        return Wcierka.objects.create(marka=marka, nazwa=nazwa)
    
    def test_kosmetyk_creation(self):
        view("Wcierka")
        WcierkaTest.create_rdz()
        w = WcierkaTest.create_kosmetyk()
        self.assertTrue(isinstance(w, Wcierka))  # , second("Wcierka"))
        self.assertEqual(w.__str__(), f"{w.marka}, {w.nazwa} ")  # , second("Wcierka"))
            

class PeelingTest(TestCase):

    @staticmethod
    def create_rdz(rodzaj="Peeling"):
        return Rdz.objects.create(rodzaj=rodzaj)
    
    @staticmethod
    def create_kosmetyk(marka="Bandi", nazwa="Tricho Esthetic Peeling"):
        return Peeling.objects.create(marka=marka, nazwa=nazwa)
    
    def test_kosmetyk_creation(self):
        view("Peeling")
        PeelingTest.create_rdz()
        w = PeelingTest.create_kosmetyk()
        self.assertTrue(isinstance(w, Peeling))  # , second("Peeling"))
        self.assertEqual(w.__str__(), f"{w.marka}, {w.nazwa} ")  # , second("Peeling"))
