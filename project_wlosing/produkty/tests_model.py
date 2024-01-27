from django.test import TestCase
from produkty.models import *


# Create your tests here.
def view(r):
    print("----------------------------------------------------------------------")
    print(f"Testing instance of {r} creation...")
def second(r):
    print( f"Error, the attempt to create an instance of {r} failed...")
class RdzTest(TestCase):    

        def create_rdz(self, Rodzaj="Olej"):
            return Rdz.objects.create(Rodzaj=Rodzaj)
        
        def test_rdz_creation(self):
                view("Rdz")
                w = self.create_rdz()
                self.assertTrue(isinstance(w, Rdz ))#, second("Rdz"))
                self.assertEqual(w.__str__(), w.Rodzaj)#, second("Rdz"))
                
                
class workingsKosmetykTest(TestCase):
    
    def create_kosmetyk(Marka="Anwen", Nazwa="Mint it up!"):
        return Kosmetyk.objects.create(Marka=Marka, Nazwa=Nazwa)
    
    
    
    def create_workingskosmetyk(self, kolejnosc, nazwa="Mint it up!"):
        return workingsKosmetyk.objects.create(kolejnosc=kolejnosc, nazwa=nazwa)

    
    def test_workings_creation(self):
            view("workingsKosmetyk")
            x = workingsKosmetykTest.create_kosmetyk()
            w = self.create_workingskosmetyk(x)
         
            self.assertTrue(isinstance(w, workingsKosmetyk))#, second("workingsKosmetyk"))
           
            self.assertEqual(w.__str__(), f"kolejnosc = {w.kolejnosc}, {w.nazwa}")#, second("workingsKosmetyk"))


class KosmetykTest(TestCase):

    def create_kosmetyk(self, Marka, Nazwa):
        return Kosmetyk.objects.create(Marka=Marka, Nazwa=Nazwa)
    
    def test_kosmetyk_creation(self):
            view("Kosmetyk")
            w = self.create_kosmetyk(Marka="Anwen", Nazwa="Mint it up!")
            self.assertTrue(isinstance(w, Kosmetyk ))#, second("Kosmetyk"))
            self.assertEqual(w.__str__(), f"{w.Marka}, {w.Nazwa} ")#, second("Kosmetyk"))

class SzamponTest(TestCase):
    
    def create_rdz( Rodzaj="Szampon"):
        return Rdz.objects.create(Rodzaj=Rodzaj)
   
    
    def create_kosmetyk(self, Marka="Anwen", Nazwa="Mint it up!", Moc="Średni"):
        return Szampon.objects.create(Marka=Marka, Nazwa=Nazwa, Moc=Moc)
    
    def test_kosmetyk_creation(self):
            view("Szampon")
            SzamponTest.create_rdz()
            w = self.create_kosmetyk()
           
            self.assertTrue(isinstance(w, Szampon ))#, second("Szampon"))
            self.assertEqual(w.__str__(), f"{w.Marka}, {w.Nazwa} ")#, second("Szampon"))
            
class OdżywkaTest(TestCase):
    
    def create_rdz( Rodzaj="Odżywka"):
        return Rdz.objects.create(Rodzaj=Rodzaj)
    
    def create_kosmetyk(self, Marka="Anwen", Nazwa="Proteinowa magnolia", PEH="Proteinowa"):
        return Odżywka.objects.create(Marka=Marka, Nazwa=Nazwa, PEH=PEH)
    
    def test_kosmetyk_creation(self):
            view("Odżywka")
            OdżywkaTest.create_rdz()    
            w = self.create_kosmetyk()
            self.assertTrue(isinstance(w, Odżywka ))#, second("Odżywka"))
            self.assertEqual(w.__str__(), f"{w.Marka}, {w.Nazwa} ")#, second("Odżywka"))
            
class MaskaTest(TestCase):
    
    def create_rdz( Rodzaj="Maska"):
        return Rdz.objects.create(Rodzaj=Rodzaj)
        
    def create_kosmetyk(self, Marka="Garnier Hair Food", Nazwa="Cocoa butter", PEH="Emolientowa"):
        return Maska.objects.create(Marka=Marka, Nazwa=Nazwa, PEH=PEH)
    
    def test_kosmetyk_creation(self):
            view("Maska")
            MaskaTest.create_rdz()  
            w = self.create_kosmetyk()
            self.assertTrue(isinstance(w, Maska ))#, second("Maska"))
            self.assertEqual(w.__str__(), f"{w.Marka}, {w.Nazwa} ")#, second("Maska"))
            
class ŻelTest(TestCase):
    
    def create_rdz( Rodzaj="Żel"):
        return Rdz.objects.create(Rodzaj=Rodzaj)
        
    def create_kosmetyk(self, Marka="Sysoss", Nazwa="Power hold", Hold="Mocny"):
        return Żel.objects.create(Marka=Marka, Nazwa=Nazwa, Hold=Hold)
    
    def test_kosmetyk_creation(self):
            view("Żel")
            ŻelTest.create_rdz()  
            w = self.create_kosmetyk()
            self.assertTrue(isinstance(w, Żel ))#, second("Żel"))
            self.assertEqual(w.__str__(), f"{w.Marka}, {w.Nazwa} ")#, second("Żel"))
            
class PiankaTest(TestCase):
    
    def create_rdz( Rodzaj="Pianka"):
        return Rdz.objects.create(Rodzaj=Rodzaj)
        
    def create_kosmetyk(self, Marka="Wella", Nazwa="Wellaflex", Hold="Mocny"):
        return Pianka.objects.create(Marka=Marka, Nazwa=Nazwa, Hold=Hold)
    
    def test_kosmetyk_creation(self):
            view("Pianka")
            PiankaTest.create_rdz()  
            w = self.create_kosmetyk()
            self.assertTrue(isinstance(w, Pianka ))#, second("Pianka"))
            self.assertEqual(w.__str__(), f"{w.Marka}, {w.Nazwa} ")#, second("Pianka"))
            
class KremTest(TestCase):
    
    def create_rdz( Rodzaj="Krem"):
        return Rdz.objects.create(Rodzaj=Rodzaj)
        
    def create_kosmetyk(self, Marka="Taft", Nazwa="Curls", Hold="Słaby"):
        return Krem.objects.create(Marka=Marka, Nazwa=Nazwa, Hold=Hold)
    
    def test_kosmetyk_creation(self):
            view("Krem")
            KremTest.create_rdz()  
            w = self.create_kosmetyk()
            self.assertTrue(isinstance(w, Krem ))#, second("Krem"))
            self.assertEqual(w.__str__(), f"{w.Marka}, {w.Nazwa} ")#, second("Krem"))
            
class OlejekTest(TestCase):
    
    def create_rdz( Rodzaj="Olejek"):
        return Rdz.objects.create(Rodzaj=Rodzaj)
        
    def create_kosmetyk(self, Marka="Isana", Nazwa="2in1 intensiv"):
        return Olejek.objects.create(Marka=Marka, Nazwa=Nazwa)
    
    def test_kosmetyk_creation(self):
            view("Olejek")
            OlejekTest.create_rdz()  
            w = self.create_kosmetyk()
            self.assertTrue(isinstance(w, Olejek ))#, second("Olejek"))
            self.assertEqual(w.__str__(), f"{w.Marka}, {w.Nazwa} ")#, second("Olejek"))
            
class OlejTest(TestCase):
    
    def create_rdz( Rodzaj="Olej"):
        return Rdz.objects.create(Rodzaj=Rodzaj)
       
    def create_kosmetyk(self, Marka="OnlyBio - Hair in balance", Nazwa="Olej do olejowania do włosów wysokoporowatych"):
        return Olej.objects.create(Marka=Marka, Nazwa=Nazwa)
    
    def test_kosmetyk_creation(self):
            view("Olej")
            OlejTest.create_rdz()  
            w = self.create_kosmetyk()
            self.assertTrue(isinstance(w, Olej ))#, second("Olej"))
            self.assertEqual(w.__str__(), f"{w.Marka}, {w.Nazwa} ")#, second("Olej"))
            

class WcierkaTest(TestCase):
    
    def create_rdz( Rodzaj="Wcierka"):
        return Rdz.objects.create(Rodzaj=Rodzaj)
    
    def create_kosmetyk(self, Marka="Anwen", Nazwa="Grow Us Tender"):
        return Wcierka.objects.create(Marka=Marka, Nazwa=Nazwa)
    
    def test_kosmetyk_creation(self):
            view("Wcierka")
            WcierkaTest.create_rdz()  
            w = self.create_kosmetyk()
            self.assertTrue(isinstance(w, Wcierka ))#, second("Wcierka"))
            self.assertEqual(w.__str__(), f"{w.Marka}, {w.Nazwa} ")#, second("Wcierka"))
            
class PeelingTest(TestCase):
    
    def create_rdz( Rodzaj="Peeling"):
        return Rdz.objects.create(Rodzaj=Rodzaj)
    
    def create_kosmetyk(self, Marka="Bandi", Nazwa="Tricho Esthetic Peeling"):
        return Peeling.objects.create(Marka=Marka, Nazwa=Nazwa)
    
    def test_kosmetyk_creation(self):
            view("Peeling")
            PeelingTest.create_rdz()  
            w = self.create_kosmetyk()
            self.assertTrue(isinstance(w, Peeling ))#, second("Peeling"))
            self.assertEqual(w.__str__(), f"{w.Marka}, {w.Nazwa} ")#, second("Peeling")) 