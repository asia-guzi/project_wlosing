from django.test import TestCase


from .models import Włosy

from .forms import WłosyForm

# models test
class WłosyTest(TestCase):

    def create_włosy(self, Długość="Krótkie", Kolor="Blond", Porowatość="Niskoporowate", Typ="Proste"):
        return Włosy.objects.create(Długość=Długość, Kolor=Kolor, Porowatość=Porowatość, Typ=Typ)
    
    def test_włosy_creation(self):
            w = self.create_włosy()
            self.assertTrue(isinstance(w, Włosy))
            self.assertEqual(w.__str__(), f"Masz {w.Długość}, {w.Kolor}, {w.Porowatość}, {w.Typ} włosy. ")
   

  