from django.db import models

from produkty.models import Kosmetyk
from typing import List


def make_list(s: str) -> list:
    """
    Converts a comma-separated string into a list of elements.

    :param s: A comma-separated string containing elements.
    :type s: str
    :return: A list containing individual elements extracted from the input string.
    :rtype: list
    """

    pass
    
    
def tlumaczenie(sklad: str) -> List[str]:
    """
    Function performing the translation of the ingredients.

    :param sklad: input sklad.
    :type: str

    :return: A list of translated ingredients.
    :rtype: list
    """
    
    sklad = make_list(sklad)
    print(f'sklad w tłumaczeniu z modelu {sklad}')
    
    PL = []
    for x in sklad:
        n = Skladnik.meaning(x)
        print(f'n = {n}')
        PL.append(n)
        
    print(f'pl = {PL}')
    return PL


class Skladnik(models.Model):
  
    inci = models.CharField(max_length=100)
    pl = models.CharField(max_length=100)

    def get_inci(self):
        return self.inci

    def get_pl(self):
        return self.pl

    def set_inci(self, inci):
        self.inci = inci

    def set_pl(self, pl):
        self.pl = pl

    def __str__(self):
        return f'{self.inci} to {self.pl}'

    @staticmethod
    def meaning(inci: str) -> str:
        """
        Assigns a value 'pl' to each ingredient 'inci'.

        :param inci: Ingredient whose meaning is to be determined.
        :type inci: str
        :return: The meaning of the ingredient 'inci'.
        :rtype: str
        """

        try:
            n = Skladnik.objects.get(inci=inci)

        except Skladnik.DoesNotExist:
            return "Error - brak składnika w bazie"

        PL = n.get_pl()

        return PL
      

class Sklad (models.Model):

    kosmetyk = models.OneToOneField(Kosmetyk, on_delete=models.CASCADE, related_name="Sklad", )
    sklad_inci = models.CharField(max_length=100)
    sklad_pl = models.CharField(max_length=100)

    def __str__(self):
        return f'Sklad : {self.sklad_inci} CZYLI {self.sklad_pl}'

    def get_sklad_inci(self):
        return self.sklad_inci

    def get_sklad_pl(self):
        return self.sklad_pl

    def set_sklad_inci(self, inci):
        self.sklad_inci = inci

    def set_sklad_pl(self, inci):
        self.sklad_pl = tlumaczenie(inci)

    def set_kosmetyk(self, kosmetyk):
        self.kosmetyk = kosmetyk

    @staticmethod
    def set_sklad(kosmetyk, inci):
        x = Sklad()
        x.set_kosmetyk(kosmetyk)
        x.set_sklad_inci(inci)
        x.set_sklad_pl(inci)
        x.save()
        return x
