from django.test import TestCase
from produkty.models import Kosmetyk, Szampon, Odżywka, Wcierka, Maska, Peeling, Żel, Pianka, Krem, Olejek, Olej, Rdz, workingsKosmetyk


# Create your tests here.

class RdzTest(TestCase):    

        def create_rdz(self, Rodzaj="Olej"):
            return Rdz.objects.create(Rodzaj=Rodzaj)
        
        def test_rdz_creation(self):
                w = self.create_rdz()
                self.assertTrue(isinstance(w, Rdz ))
                self.assertEqual(w.__str__(), w.Rodzaj)
                
                
class workingsKosmetykTest(TestCase):
    
    def create_kosmetyk(Marka="Anwen", Nazwa="Mint it up!"):
        return Kosmetyk.objects.create(Marka=Marka, Nazwa=Nazwa)
    
    
    
    def create_workingskosmetyk(self, kolejnosc, nazwa="Mint it up!"):
        return workingsKosmetyk.objects.create(kolejnosc=kolejnosc, nazwa=nazwa)

    
    def test_workings_creation(self):
            x = workingsKosmetykTest.create_kosmetyk()
            w = self.create_workingskosmetyk(x)
         
            self.assertTrue(isinstance(w, workingsKosmetyk))
           
            self.assertEqual(w.__str__(), f"kolejnosc = {w.kolejnosc}, {w.nazwa}")


class KosmetykTest(TestCase):

    def create_kosmetyk(self, Marka, Nazwa):
        return Kosmetyk.objects.create(Marka=Marka, Nazwa=Nazwa)
    
    def test_kosmetyk_creation(self):
            w = self.create_kosmetyk(Marka="Anwen", Nazwa="Mint it up!")
            self.assertTrue(isinstance(w, Kosmetyk ))
            self.assertEqual(w.__str__(), f"{w.Marka}, {w.Nazwa} ")

class SzamponTest(TestCase):
    
    def create_rdz( Rodzaj="Szampon"):
        return Rdz.objects.create(Rodzaj=Rodzaj)
   
    
    def create_kosmetyk(self, Marka="Anwen", Nazwa="Mint it up!", Moc="Średni"):
        return Szampon.objects.create(Marka=Marka, Nazwa=Nazwa, Moc=Moc)
    
    def test_kosmetyk_creation(self):
            SzamponTest.create_rdz()
            w = self.create_kosmetyk()
           
            self.assertTrue(isinstance(w, Szampon ))
            self.assertEqual(w.__str__(), f"{w.Marka}, {w.Nazwa} ")
            
class OdżywkaTest(TestCase):
    
    def create_rdz( Rodzaj="Odżywka"):
        return Rdz.objects.create(Rodzaj=Rodzaj)
    
    def create_kosmetyk(self, Marka="Anwen", Nazwa="Proteinowa magnolia", PEH="Proteinowa"):
        return Odżywka.objects.create(Marka=Marka, Nazwa=Nazwa, PEH=PEH)
    
    def test_kosmetyk_creation(self):
            OdżywkaTest.create_rdz()    
            w = self.create_kosmetyk()
            self.assertTrue(isinstance(w, Odżywka ))
            self.assertEqual(w.__str__(), f"{w.Marka}, {w.Nazwa} ")
            
class MaskaTest(TestCase):
    
    def create_rdz( Rodzaj="Maska"):
        return Rdz.objects.create(Rodzaj=Rodzaj)
        
    def create_kosmetyk(self, Marka="Garnier Hair Food", Nazwa="Cocoa butter", PEH="Emolientowa"):
        return Maska.objects.create(Marka=Marka, Nazwa=Nazwa, PEH=PEH)
    
    def test_kosmetyk_creation(self):
            MaskaTest.create_rdz()  
            w = self.create_kosmetyk()
            self.assertTrue(isinstance(w, Maska ))
            self.assertEqual(w.__str__(), f"{w.Marka}, {w.Nazwa} ")
            
class ŻelTest(TestCase):
    
    def create_rdz( Rodzaj="Żel"):
        return Rdz.objects.create(Rodzaj=Rodzaj)
        
    def create_kosmetyk(self, Marka="Sysoss", Nazwa="Power hold", Hold="Mocny"):
        return Żel.objects.create(Marka=Marka, Nazwa=Nazwa, Hold=Hold)
    
    def test_kosmetyk_creation(self):
            ŻelTest.create_rdz()  
            w = self.create_kosmetyk()
            self.assertTrue(isinstance(w, Żel ))
            self.assertEqual(w.__str__(), f"{w.Marka}, {w.Nazwa} ")
            
class PiankaTest(TestCase):
    
    def create_rdz( Rodzaj="Pianka"):
        return Rdz.objects.create(Rodzaj=Rodzaj)
        
    def create_kosmetyk(self, Marka="Wella", Nazwa="Wellaflex", Hold="Mocny"):
        return Pianka.objects.create(Marka=Marka, Nazwa=Nazwa, Hold=Hold)
    
    def test_kosmetyk_creation(self):
            PiankaTest.create_rdz()  
            w = self.create_kosmetyk()
            self.assertTrue(isinstance(w, Pianka ))
            self.assertEqual(w.__str__(), f"{w.Marka}, {w.Nazwa} ")
            
class KremTest(TestCase):
    
    def create_rdz( Rodzaj="Krem"):
        return Rdz.objects.create(Rodzaj=Rodzaj)
        
    def create_kosmetyk(self, Marka="Taft", Nazwa="Curls", Hold="Słaby"):
        return Krem.objects.create(Marka=Marka, Nazwa=Nazwa, Hold=Hold)
    
    def test_kosmetyk_creation(self):
            KremTest.create_rdz()  
            w = self.create_kosmetyk()
            self.assertTrue(isinstance(w, Krem ))
            self.assertEqual(w.__str__(), f"{w.Marka}, {w.Nazwa} ")
            
class OlejekTest(TestCase):
    
    def create_rdz( Rodzaj="Olejek"):
        return Rdz.objects.create(Rodzaj=Rodzaj)
        
    def create_kosmetyk(self, Marka="Isana", Nazwa="2in1 intensiv"):
        return Olejek.objects.create(Marka=Marka, Nazwa=Nazwa)
    
    def test_kosmetyk_creation(self):
            OlejekTest.create_rdz()  
            w = self.create_kosmetyk()
            self.assertTrue(isinstance(w, Olejek ))
            self.assertEqual(w.__str__(), f"{w.Marka}, {w.Nazwa} ")
            
class OlejTest(TestCase):
    
    def create_rdz( Rodzaj="Olej"):
        return Rdz.objects.create(Rodzaj=Rodzaj)
       
    def create_kosmetyk(self, Marka="OnlyBio - Hair in balance", Nazwa="Olej do olejowania do włosów wysokoporowatych"):
        return Olej.objects.create(Marka=Marka, Nazwa=Nazwa)
    
    def test_kosmetyk_creation(self):
            OlejTest.create_rdz()  
            w = self.create_kosmetyk()
            self.assertTrue(isinstance(w, Olej ))
            self.assertEqual(w.__str__(), f"{w.Marka}, {w.Nazwa} ")
            

class WcierkaTest(TestCase):
    
    def create_rdz( Rodzaj="Wcierka"):
        return Rdz.objects.create(Rodzaj=Rodzaj)
    
    def create_kosmetyk(self, Marka="Anwen", Nazwa="Grow Us Tender"):
        return Wcierka.objects.create(Marka=Marka, Nazwa=Nazwa)
    
    def test_kosmetyk_creation(self):
            WcierkaTest.create_rdz()  
            w = self.create_kosmetyk()
            self.assertTrue(isinstance(w, Wcierka ))
            self.assertEqual(w.__str__(), f"{w.Marka}, {w.Nazwa} ")
            
class PeelingTest(TestCase):
    
    def create_rdz( Rodzaj="Peeling"):
        return Rdz.objects.create(Rodzaj=Rodzaj)
    
    def create_kosmetyk(self, Marka="Bandi", Nazwa="Tricho Esthetic Peeling"):
        return Peeling.objects.create(Marka=Marka, Nazwa=Nazwa)
    
    def test_kosmetyk_creation(self):
            PeelingTest.create_rdz()  
            w = self.create_kosmetyk()
            self.assertTrue(isinstance(w, Peeling ))
            self.assertEqual(w.__str__(), f"{w.Marka}, {w.Nazwa} ") 