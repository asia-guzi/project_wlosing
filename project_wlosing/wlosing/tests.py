from django.test import TestCase

from .models import Wlosy


# models test
class WlosyTest(TestCase):

    @staticmethod
    def create_wlosy(dlugosc="Krótkie", kolor="Blond", porowatosc="Niskoporowate", typ="Proste"):
        return Wlosy.objects.create(dlugosc=dlugosc, kolor=kolor, porowatosc=porowatosc, typ=typ)
    
    def test_wlosy_creation(self):
        w = self.create_wlosy()
        self.assertTrue(isinstance(w, Wlosy))
        self.assertEqual(w.__str__(), f"Masz {w.dlugosc}, {w.kolor}, {w.porowatosc}, {w.typ} włosy. ")


  