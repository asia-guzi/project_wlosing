from django.test import TestCase
from .models import Składnik, Skład, tłumaczenie, make_list
from produkty.models import Kosmetyk


# Create your tests here.

def set_Kosmetyk(Marka, Nazwa):
    x=Kosmetyk()
    x.set_Marka(Marka)
    x.set_Nazwa(Nazwa)
    x.save()
    return x

class SkładnikTest(TestCase):    

        def create_składnik(self, INCI, PL):
            return Składnik.objects.create(INCI=INCI, PL=PL)
        
        def test_składnik_creation(self):
                w = self.create_składnik(INCI="Cetracyl Alcohol", PL="Alkohol tłuszczowy")
                self.assertTrue(isinstance(w, Składnik ))
                self.assertEqual(w.__str__(), f'{w.INCI} to {w.PL}')
                
# class SkładTest(TestCase):    
        


#         def create_skład(self, Kosmetyk, skład_INCI, skład_PL):
#             return Skład.objects.create(Kosmetyk=Kosmetyk, skład_INCI=skład_INCI, skład_PL=skład_PL)
            
           
        
#         def test_skład_creation(self):
                
#                 Kosmetyk = set_Kosmetyk("Anwen", "Mint it up!")
              
                
#                 a = SkładnikTest.create_składnik(Składnik(), INCI="Cetracyl Alcohol", PL="Alkohol tłuszczowy")
#                 b = SkładnikTest.create_składnik(Składnik(), INCI="Glycerin", PL="Gliceryna (H)")
#                 print(f"a,b' {a, b}")
                
#                 skład_INCI="Cetracyl Alcohol, Glycerin"
#                 skład_PL=tłumaczenie(skład_INCI)
#                 print(f'kosmetyk, inci, pl = {Kosmetyk, skład_INCI, skład_PL}')
                
                
#                 w = self.create_skład(Kosmetyk=Kosmetyk, skład_INCI=skład_INCI, skład_PL=skład_PL)
#                 self.assertTrue(isinstance(w, Skład ))               
#                 self.assertEqual(w.__str__(), f'Skład : {self.skład_INCI} CZYLI {self.skład_PL}')
