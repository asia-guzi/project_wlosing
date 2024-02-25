from django.test import TestCase
from .models import Skladnik, Sklad, tlumaczenie, make_list
from produkty.models import Kosmetyk


# Create your tests here.

def set_kosmetyk(marka, nazwa):
    x = Kosmetyk()
    x.set_marka(marka)
    x.set_nazwa(nazwa)
    x.save()
    return x


class SkladnikTest(TestCase):

    @staticmethod
    def create_skladnik(inci, pl):
        return Skladnik.objects.create(INCI=inci, PL=pl)

    def test_skladnik_creation(self):
        w = self.create_skladnik(inci="Cetracyl Alcohol", pl="Alkohol tłuszczowy")
        self.assertTrue(isinstance(w, Skladnik))
        self.assertEqual(w.__str__(), f'{w.inci} to {w.pl}')

# class SkładTest(TestCase):    


#         def create_skład(self, kosmetyk, sklad_inci, sklad_pl):
#             return Sklad.objects.create(kosmetyk=kosmetyk, sklad_inci=sklad_inci, sklad_pl=sklad_pl)
           
        
#         def test_skład_creation(self):
                
#                 kosmetyk = set_kosmetyk("Anwen", "Mint it up!")
              
                
#                 a = SkladnikTest.create_skladnik(Skladnik(), inci="Cetracyl Alcohol", pl="Alkohol tłuszczowy")
#                 b = SkladnikTest.create_skladnik(Skladnik(), inci="Glycerin", pl="Gliceryna (H)")
#                 print(f"a,b' {a, b}")
                
#                 sklad_inci="Cetracyl Alcohol, Glycerin"
#                 sklad_pl=tlumaczenie(sklad_inci)
#                 print(f'kosmetyk, inci, pl = {kosmetyk, sklad_inci, sklad_pl}')
                
                
#                 w = self.create_skład(kosmetyk=kosmetyk, sklad_inci=sklad_inci, sklad_pl=sklad_pl)
#                 self.assertTrue(isinstance(w, Sklad ))
#                 self.assertEqual(w.__str__(), f'Sklad : {self.sklad_inci} CZYLI {self.sklad_pl}')
