from django.contrib.auth.models import User
from django.db import models
from project_wlosing import settings
from typing import Union, Tuple


class Wlosy(models.Model):
  
    DLUGOSC_CHOICES = [
        ("Krótkie", "Krótkie - do ramion"),
        ("Średnie", "Średnie - za ramiona"),
        ("Długie", "Długie - za łopatki"),
        ]

    KOLOR_CHOICES = [
        ("Blond", "Blond"),
        ("Szatynka", "Szatynka"),
        ("Brunetka", "Brunetka"),
        ("Rude", "Rude"),
        ]
    POROWATOSC_CHOICES = [
        ("Wysokoporowate", "Wysokoporowate"),
        ("Średnioporowate", "Średnioporowate"),
        ("Niskoporowate", "Niskoporowate"),
        ]
    TYP_CHOICES = [
        ("Proste", "Proste - brak skrętu"),
        ("Falowane", "Falowane - typ 2a, 2b lub 2c"),
        ("Wurly", "Wurly - uzupełnij"),
        ("Kręcone", "Kręcone - typ 3a, 3b lub 3c"),
        ("Afro", "Afro - typ 4"),
        ]

    dlugosc = models.CharField(max_length=100, choices=DLUGOSC_CHOICES)
    kolor = models.CharField(max_length=100, choices=KOLOR_CHOICES)
    porowatosc = models.CharField(max_length=100, choices=POROWATOSC_CHOICES)
    typ = models.CharField(max_length=100, choices=TYP_CHOICES)
    owner = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="typ_wlosow", blank=True)

    def __str__(self):
        return f"Masz {self.dlugosc}, {self.kolor}, {self.porowatosc}, {self.typ} włosy. "

    def get_dlugosc(self):
        return self.dlugosc

    def get_kolor(self):
        return self.kolor

    def get_porowatosc(self):
        return self.porowatosc

    def get_typ(self):
        return self.typ

    def set_dlugosc(self, dlugosc: str):
        self.dlugosc = dlugosc

    def set_kolor(self, kolor: str):
        self.kolor = kolor

    def set_porowatosc(self, porowatosc: str):
        self.porowatosc = porowatosc

    def set_typ(self, typ: str):
        self.typ = typ

    def set_all(self, dlugosc: str, kolor: str, porowatosc: str, typ: str):
        self.set_dlugosc(dlugosc)
        self.set_kolor(kolor)
        self.set_porowatosc(porowatosc)
        self.set_typ(typ)

    @staticmethod
    def get_info(user: User, check: bool = False) \
            -> Union['Wlosy', Tuple['Wlosy', bool], str, Tuple[str, bool]]:

        """Retrieves information about the user's hair.

        :param user: The user instance to retrieve information for.
        :type user: User
        :param check: "Determines whether the function should return only the output or both
        the output and a boolean (if true).".
        :type check: bool, optional
        :return: If `check` is True, returns an instance of the 'Wlosy' class representing
            the user's hair details and bool value or information that hair does not exist.
            If `check` is False or result contains no boolean.
        :rtype: Union[Wlosy, str]
        """

        a = ("Upss... Nie uzupełniłaś podstawowych informacji o swoich włosach! "
             "Dodaj je aby móc w pełnin korzystać ze strony:")

        if check:
            if user.typ_wlosow.exists():
                return user.typ_wlosow.last(), True
            else:
                return a, False
        else:
            if user.typ_wlosow.exists():
                print(user.typ_wlosow.last())
                return user.typ_wlosow.last()
            else:
                return a

# class porowatosc (Wlosy):

      
#       Właściwość = models.ForeignKey(Wlosy, to_field="porowatosc", on_delete=models.CASCADE)

#       * = models.ForeignKey(porowatosc, related_name="porowatosc")
      
#       '''TBC - użyć jako foreignkey dla modelu Wlosy |opis, hierarchia_PEH'''
        # """+ odnosniki do pielegnacji i odzywek"""
      
# class typ (Wlosy):
#     
#             * = models.ForeignKey(typ, related_name="typ")
              
#             """ jw + odnoniki do stylizacji"""

# class rodzaj (porowatosc, typ):
    
