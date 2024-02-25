from django.shortcuts import render
from .forms import *
from django.http import HttpResponse, HttpRequest
from produkty.models import *
from django import forms
from wlosing.views import WlosingViews
from users.views import login_view
from django.views import View
from typing import Any


def ustal_form(r: str, post: Any = None) -> forms.Form:
    """
    Determines the appropriate form based on the given category.

    This function determines the appropriate form based on the given product category.

    :param r: The product category.
    :type r: str
    :param post: Additional data passed as POST data (default is None).
    :type post: Any

    :return: An instance of the specific form based on the provided category.
    :rtype: Form
    """

    form_mapping = {
        "Szampon": SzamponForm,
        "Odzywka": OdzywkaForm,
        "Maska": MaskaForm,
        "Wcierka": WcierkaForm,
        "Pianka": PiankaForm,
        "Zel": ZelForm,
        "Krem": KremForm,
        "Peeling": PeelingForm,
        "Olej": OlejForm,
        "Olejek": OlejekForm,
    }

    if post:
        return form_mapping[r](post)

    return form_mapping[r]()
            

def zmienna_ustal(d: dict = {}) -> dict:
    """
    Determines product categories and their respective lists.

    This function determines product categories and their respective lists by iterating through available
    categories.
    It uses the `lista_ustal` function to retrieve the product list for each category.

    :param d: A dictionary to store product categories and their respective lists
              (initial elements of dictionary in the end are also shown on the view).
    :type d: dict

    :return: A dictionary representing all cosmetics ever added to the project.
             It contains product categories as keys and their respective lists as values.
    :rtype: dict
    """

    for r in Rdz.rdz_list():

        v = Kosmetyk.kosmetyk_list(r)

        if v != []:
            d[r] = v

    return d


class ProduktyViews(View):

    @staticmethod
    def pindex(request, info=None):
        zmienna = zmienna_ustal()
        zmienna["form"] = RdzForm()
        zmienna["info"] = info

        return render(request, "produkty/indexcopy.html", zmienna)

    @staticmethod
    def addk_view(request, r, info=None):
        zmienna = {"form": ustal_form(r)}

        if info:
            zmienna["info"] = info

        return render(request, "produkty/addk.html",  zmienna)
                   

def wydziel(x: str) -> str:
    """
    Extracts the last element from a comma-separated string.

    This function takes a comma-separated string (string representation of cosmetics list "marka, nazwa")
    and extracts the last element, which is the name (nazwa).

    :param x: The comma-separated string.
    :type x: str

    :return: The last element from the comma-separated string, which is the cosmetic's name.
    :rtype: str
    """
    
    y = x.split(", ")
    return y[-1]


def obecnosc_ustal(r: str, n: str) -> bool:
    """
    Determines if an object defined by the given name already exists in the database.

    This function determines if the product has already been added to the database based on the given product name.

    :param r: The product category.
    :type r: str
    :param n: The product name.
    :type n: str

    :return: True if the product already exists in the database and False if it is new.
    :rtype: bool
    """

    n_mapping = Kosmetyk.kosmetyk_map(r)

    try:
        n_mapping.objects.get(nazwa=n)
    except n_mapping.DoesNotExist:
        return False
    return True


def index(request: HttpRequest) -> HttpResponse:
    """
    Handles the basic cosmetics collection view.

    This function shows the basic cosmetics collection view.
    It creates the variable r assigned to the session which represents the product category.
    It also allows authenticated users to start adding new product to the database based on session variable.

    :param request: The HTTP request object.
    :type request: HttpRequest

    :return: The HTTP response to be displayed.
    :rtype: HttpResponse
    """

    if request.method == "POST":
        form = RdzForm(request.POST)
        if form.is_valid():
            r = request.POST["Rdz"]
            request.session["r"] = r

            return ProduktyViews.addk_view(request, r)

        else:

            info = "Upsss... coś poszło nie tak"
            return ProduktyViews.pindex(request, info)

    else:
        return ProduktyViews.pindex(request)
                          
               
def addk(request: HttpRequest) -> HttpResponse:
    """
    Handles adding new cosmetics to the database.

    This function allows authenticated users to add new cosmetics to the database.
    It checks if the session variable "r" exists within the session.
    Then the obecnosc_ustal() function is used to verify if the cosmetics has already been added.
    If the given conditions are fulfilled, the new cosmetic is added.

    :param request: The HTTP request object.
    :type request: HttpRequest

    :return: The HTTP response to be displayed.
    :rtype: HttpResponse
    """

    if not request.user.is_authenticated:

        message = "Zaloguj się, aby dodać produkt do bazy"
        return login_view(request, message)

    try:
        r = request.session["r"]

    except KeyError:
        return ProduktyViews.pindex(request, "Error - brak rodzaju")

    if request.method == "POST":
        x = request.POST["nazwa"]

        if obecnosc_ustal(r, x):

            info = f"Upsss... Ten kosmetyk ({x}) jest już w naszej bazie. Możesz zasilić nim swoją kosmetyczkę"
            return ProduktyViews.pindex(request, info)

        else:
            pass
        """sprawdzić czy form is valid"""

        q = ustal_form(r, request.POST)

        if q.is_valid():
            pass

        else:
            info = "Upsss... coś poszło nie tak"
            return ProduktyViews.addk_view(request, r, info)

        k = q.save()
        k.set_owner(request.user)
        WorkingsKosmetyk.set_work(k)

        info = "Baza zasilona"
        return ProduktyViews.pindex(request, info)
   
    else:
        info = "nie ta metoda"
        return ProduktyViews.addk_view(request, r, info)

        
def jeden(request: HttpRequest, nazwa: str) -> HttpResponse:
    """
    Handles adding a product to the user's cosmetic collection.

    This function allows authenticated users to add a product to their cosmetic collection.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :param nazwa: The product name.
    :type nazwa: str
    :param button: Information if button "add" should be displayed.
    :type button: bool

    :return: The HTTP response to be displayed (the view unique based on cosmetics name).
    :rtype: HttpResponse
    """

    if not request.user.is_authenticated:
        return login_view(request, "Zaloguj się, aby dodać produkt do swojej kosmetyczki")

    class Roboczy (forms.Form):
        N = forms.CharField(widget=forms.HiddenInput(), initial=nazwa)

    if request.method == "POST":
        form = Roboczy(request.POST)
        if form.is_valid():
            nazwa = wydziel(request.POST["N"])
            owner = request.user
            a = owner.wKosmetyczce.filter(nazwa=nazwa)

            if a.exists():
                mess = "Sprawdź dokładniej, ten kosmetyk znajduje się już w Twojej kosmetyczce."
                return WlosingViews.inform(request, mess)

            try:
                q = Kosmetyk.objects.get(nazwa=nazwa)
            except Kosmetyk.DoesNotExist:
                mess = "Sprawdź dokładniej, ten kosmetyk znajduje się już w Twojej kosmetyczce."
                return WlosingViews.inform(request, mess)

            q.set_owner(owner)

            mess = "Gratulacje, Kosmetyczka zasilona!"
            return WlosingViews.inform(request, mess)

    else:
        name = wydziel(nazwa)
        name.capitalize()
        context = {'name': name}
        context['form'] = Roboczy()

        return render(request, "produkty/jeden.html", context)
