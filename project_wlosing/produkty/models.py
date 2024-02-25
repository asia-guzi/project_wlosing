from typing import Tuple, Union, Callable, Optional, List
from django.contrib.auth.models import User
from django.db import models
from django.db.models.query import QuerySet

from project_wlosing import settings
from django import forms


class Rdz (models.Model):
                       
    rodzaj = models.CharField(max_length=100, unique=True)

    def set_rodzaj(self, rdz: str):
        self.rodzaj = rdz

    def get_rodzaj(self):
        return self.rodzaj

    def __str__(self):
        return f"{self.rodzaj}"

    @staticmethod
    def rdz_list():
        return [r.rodzaj for r in Rdz.objects.all()]


class Kosmetyk(models.Model):

    marka = models.CharField(max_length=100)
    nazwa = models.CharField(max_length=100)
    owner = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="wKosmetyczce", blank=True)

    def get_marka(self):
        return self.marka

    def get_nazwa(self):
        return self.nazwa

    def get_owner(self):
        return self.owner

    def set_marka(self, m: str):
        self.marka = m

    def set_nazwa(self, n: str):
        self.nazwa = n

    def set_owner(self, o: User):
        self.owner.add(o)

    def __str__(self):
        return f"{self.marka}, {self.nazwa} "

    @staticmethod
    def kosmetyk_map(r: str) -> Union['Szampon', 'Odzywka', 'Krem']:
        """
        Maps the type of cosmetic to the corresponding object.

        This function maps the type of cosmetic specified by the input string `r` to the corresponding
        object representing that cosmetic type. It returns the object representing the cosmetic type if
        found, or None if no matching object is found.

        :param r: The string representing the type of cosmetic.
        :type r: str

        :return: The object representing the cosmetic type if found, or None otherwise.
        :rtype: one of the Kosmetyk's childclasses
        """
        mapping = {
                "Szampon": Szampon,
                "Odzywka": Odzywka,
                "Maska": Maska,
                "Wcierka": Wcierka,
                "Pianka": Pianka,
                "Zel": Zel,
                "Krem": Krem,
                "Peeling": Peeling,
                "Olej": Olej,
                "Olejek": Olejek,
            }
        return mapping[r]

    @staticmethod
    def kosmetyk_list(r: str) -> List:
        """
        Determines the appropriate cosmetics list based on the given category.

        This static method determines the appropriate list of cosmetics based on the provided product category.
        If the category is None, it returns a list of all cosmetics in the database.

        :param r: The product category.
        :type r: str or None

        :return: An instance of the specific form based on the provided category.
        :rtype: List
        """

        try:
            k = Kosmetyk.kosmetyk_map(r).objects.all()
        except AttributeError:
            return []

        return [f"{x.get_marka()}, {x.get_nazwa()}" for x in k]

    @staticmethod
    def get_kosmetyczka(user: User, check: bool = False) \
            -> Union[QuerySet, Tuple[QuerySet, bool], str, Tuple[str, bool]]:
        """
        Retrieves the cosmetic data associated with the given user.

        This static method retrieves the cosmetic data associated with the provided user.

        :param user: The user for whom cosmetic data is retrieved.
        :type user: User
        :param check: Flag indicating whether to perform a validity check (default is False).
        :type check: bool

        :return: If `check` is False, returns the queryset containing cosmetic data for the user.
                 If `check` is True, returns a tuple containing the queryset and a boolean value
        :rtype: Union[QuerySet, Tuple[QuerySet, bool]]
        """

        try:
            y = user.wKosmetyczce.all()

        except AttributeError:
            x = "Twoja kosmetyczka niestety jest pusta!"

            if check:
                return x, False
            else:
                return x
        else:
            if check:
                return y, True
            else:
                return y

    class Meta:
        verbose_name_plural = "Kosmetyki"

    # def get_skład(self, name):
    #     """wsywietla sklad kosmetyku który jest w bazie"""
    #     try:
    #         x = Sklad.objects.get(name=name)
    #
    #     except: return "Error"
    #
    #     inci = x.inci
    #     pl = x.pl
    # #     return ( inci, pl)
    #
    #
    # def get_skład(self):
    #     return self.Sklad #lub skorzysta z related name
   

class WorkingsKosmetyk(models.Model):
     
    """unregistered model"""

    kolejnosc = models.OneToOneField(Kosmetyk, on_delete=models.CASCADE)
    nazwa = models.CharField(max_length=100)

    def __str__(self):
        return f"kolejnosc = {self.kolejnosc}, {self.nazwa}"

    def get_kolejnosc(self):
        return self.kolejnosc

    def get_nazwa(self):
        return self.nazwa

    def set_kolejnosc(self, kosmetyk: 'Kosmetyk'):
        self.kolejnosc = kosmetyk

    def set_nazwa(self, n: str):
        self.nazwa = n

    @staticmethod
    def set_work(x: Kosmetyk) -> 'WorkingsKosmetyk':
        """
        Sets the new WorkingsKosmetyk based on the provided kosmetyk item.

        This method creates a new instance of WorkingsKosmetyk with a one-to-one
        relationship with the given kosmetyk instance
        and saves it.

        :param x: The kosmetyk object to base the new WorkingsKosmetyk instance on.
        :type x: Kosmetyk

        :return: The newly created instance of WorkingsKosmetyk.
        :rtype: WorkingsKosmetyk
        """
        q = WorkingsKosmetyk()
        q.set_kolejnosc(x)
        q.set_nazwa(f"{x.nazwa}.{x.marka}")
        q.save()
        return q

    @staticmethod
    def check_b(name: str, nazwa: str, t: int = 0, index: Optional[int] = None) -> Union[bool, Callable]:
        """
        Checks which one of the words 'name' and 'nazwa' is earlier in the sorted list.

        This function compares the alphabetical order of the letters at index 't' in the words 'name' and 'nazwa'.
        If the letters are the same, the function recursively checks the following letter.

        :param name: The name of the cosmetic searched for.
        :type name: str
        :param nazwa: The name of the cosmetic chosen to compare using bisection search.
        :type nazwa: str
        :param t: The index of the letter to be checked (default is 0).
        :type t: int, optional
        :param index: The length of the strings 'name' and 'nazwa' (default is None).
        :type index: int, optional

        :return:
            - True if name[t] is earlier in alphabet (hence name is earlier than nazwa),
            - False if name[t] is later in alphabet,
            - Recursion if letters are the same.
        :rtype: Union[bool, Callable]
        """
        # establish max index resulting from the shorter word
        if t == 0:
            a = len(name)
            b = len(nazwa)

            if a < b:
                index = a-1
            else:
                index = b-1

        # if based on letter at index t, the name is earlier in the alphabet return true
        if name[t] < nazwa[t]:
            return True

        # if based on letter at index t, the name is later in the alphabet return false
        elif name[t] > nazwa[t]:
            return False

        # if letters are the same - check the next letter or if it is the last letter -
        # return longer word as later in alphabet
        else:
            if t == index:
                if len(name) < len(nazwa):
                    return True
                else:
                    return False

            return WorkingsKosmetyk.check_b(name, nazwa, t + 1, index)

    @staticmethod
    def bisection(name: str, lista: list) -> Callable:
        """
        Bisection search for cosmetics.

        This function performs the bisection search on alphabetically ordered WorkingsKosmetyk based on the given name.
        It uses the check_b() function to establish if the given name should be in the first or second half  of the list
        and looks for the cosmetic name in that part

        :param name: The name of the cosmetic.
        :type name: str
        :param lista: The list of all cosmetics in WorkingsKosmetyk (or cosmetics yet unrejected).
        :type lista: list

        :return: A callable object.
        :rtype: Callable
        """

        # get copy of analysed list of cosmetics
        lista_bi = lista.copy()

        # dlugosc is a lenght of analyzed list
        dlugosc = len(lista_bi)

        # if analysed list is longer then 2 elements - function finds the index of the word in the middle of the list
        if dlugosc > 2:
            pozycja_p = [int((dlugosc-1)/2)]

        # if lenght of the list is 2 function checkes both words
        elif dlugosc == 2:
            pozycja_p = [0, 1]

        # if lenght of the list is 1 - function checkes the only word
        else:
            pozycja_p = [0]

        for p in pozycja_p:
            # x is the word from the WorkingCosmetic from list
            x = lista_bi[p]

            # is the name of workingscosmetic beeing compared to the searched name
            nazwa = x.nazwa

            """tutaj coś trzeba począć z tą listą == 2"""
            # if the workingscosmetic corresponding to searched name is found -
            # function returns PK of orginal Cosmetic object matched with that name

            if name == nazwa:
                return x.kolejnosc

        # otherwise call the function to derermine which word is earlier in alphabet
        # (true if name is earlier, false else)

        # if name (analysed) is earlier in alfabet than nazwa (compared) -
        # further search performed only on the first half of original list (deletion of second half)
        if WorkingsKosmetyk.check_b(name, nazwa):
            del lista_bi[pozycja_p:]

        # if name (analysed) is later in alfabet than nazwa (compared) -
        # further search performed only on the second half of original list (deletion of first half)
        else:
            del lista_bi[:pozycja_p]

        return WorkingsKosmetyk.bisection(name, lista_bi)

    @staticmethod
    def get_pk(name: str) -> int:
        """
        Allows to identify the position of a cosmetic in the database.

        This function identifies the position of a cosmetic in the database
        based on the name, and the working model 'WorkingsKosmetyk'.

        :param name: The name of the cosmetic.
        :type name: str

        :return: The position of the cosmetic in the database.
        :rtype: int
        """

        lista = WorkingsKosmetyk.objects.all()
        kosmetyk = WorkingsKosmetyk.bisection(name, lista)

        pk = kosmetyk.id

        return pk

    class Meta:
        ordering = ['nazwa']
                

class Szampon (Kosmetyk):

    MOC_CHOICES = [
        ("Łagodny", "Łagodny"),
        ("Średni", "Średni"),
        ("Rypacz (mocny)", "Rypacz (mocny)"),
        ]

    rodzaj = models.ForeignKey(Rdz, to_field="rodzaj", on_delete=models.CASCADE, related_name="szampony",
                               default="Szampon")
    moc = models.CharField(max_length=100, choices=MOC_CHOICES)

    def get_moc(self):
        return self.moc

    def set_moc(self, m):
        self.moc = m

    class Meta:
        verbose_name_plural = "Szampony"


class OM (Kosmetyk):
    
    PEH_CHOICES = {
        ("Emolientowa", "Emolientowa"),
        ("Proteinowa", "Proteinowa"),
        ("Humektantowa", "Humektantowa"),
        ("PEH'owa", "PEH"),
        ("Emolientowo - humektantowa", "EH"),
        ("Humektantowo - emolientowa", "HE")
        }

    PEH = models.CharField(max_length=100, choices=PEH_CHOICES)
    
    def get_peh(self):
        return self.owner

    def set_peh(self, m):
        self.PEH = m

    class Meta:
        abstract = True


class Odzywka (OM):

    Rodzaj = models.ForeignKey(Rdz, to_field="rodzaj", on_delete=models.CASCADE, related_name="Odzywki",
                               default="Odzywka")

    class Meta:
        verbose_name_plural = "Odzywki"


class Maska (OM):
        
    Rodzaj = models.ForeignKey(Rdz, to_field="rodzaj", on_delete=models.CASCADE, related_name="Maski",
                               default="Maska")

    class Meta:
        verbose_name_plural = "Maski"


class Stylizator (Kosmetyk):
    HOLD_CHOICES = [
        ("Lekki", "Lekki"),
        ("Średni", "Średni"),
        ("Mocny", "Mocny"),
        ]

    hold = models.CharField(max_length=100, choices=HOLD_CHOICES)
    
    def get_hold(self):
        return self.owner

    def set_hold(self, m):
        self.hold = m

    class Meta:
        verbose_name_plural = "Stylizatory"

    
class Zel (Stylizator):
    
    Rodzaj = models.ForeignKey(Rdz, to_field="rodzaj", on_delete=models.CASCADE, related_name="Zele",
                               default="Zel")
        
    class Meta:
        verbose_name_plural = "Zele"


class Pianka (Stylizator):
    
    Rodzaj = models.ForeignKey(Rdz, to_field="rodzaj", on_delete=models.CASCADE, related_name="Pianki",
                               default="Pianka")

    class Meta:
        verbose_name_plural = "Pianki"


class Krem (Stylizator):

    Rodzaj = models.ForeignKey(Rdz, to_field="rodzaj",  on_delete=models.CASCADE, related_name="Kremy",
                               default="Krem")

    class Meta:
        verbose_name_plural = "Kremy"


class Olej (Kosmetyk):
    
    Rodzaj = models.ForeignKey(Rdz, to_field="rodzaj", on_delete=models.CASCADE, related_name="Oleje",  default="Olej")
        
    class Meta:
        verbose_name_plural = "Oleje"


class Olejek (Kosmetyk):
    
    Rodzaj = models.ForeignKey(Rdz, to_field="rodzaj", on_delete=models.CASCADE, related_name="Olejki",
                               default="Olejek")
  
    class Meta:
        verbose_name_plural = "Olejki"


class Wcierka (Kosmetyk):
    
    Rodzaj = models.ForeignKey(Rdz, to_field="rodzaj", on_delete=models.CASCADE, related_name="Wcierki",
                               default="Wcierka")
        
    class Meta:
        verbose_name_plural = "Wcierki"


class Peeling (Kosmetyk):
    
    Rodzaj = models.ForeignKey(Rdz, to_field="rodzaj", on_delete=models.CASCADE, related_name="Peelingi",
                               default="Peeling")

    class Meta:
        verbose_name_plural = "Peelingi"
