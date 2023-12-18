from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .forms import RdzForm, SzamponForm, OdżywkaForm, WcierkaForm, MaskaForm, PeelingForm, ŻelForm, PiankaForm, KremForm, OlejekForm, OlejForm 

from produkty.models import Kosmetyk, Szampon, Odżywka, Wcierka, Maska, Peeling, Żel, Pianka, Krem, Olejek, Olej, Rdz, workingsKosmetyk
from django import forms
from wlosing.models import Włosy
from wlosing.views import wlosing_views
from users.views import  login_view
from django.views import View

def zmienna_ustal(d={}):

    """
    Determines product categories and their respective lists.
    
    This function determines product categories and their respective lists by iterating through available categories.
    It uses the `lista_ustal` function to retrieve the product list for each category.
    
    Parameters:
    d (dict): A dictionary to store product categories and their respective lists 
    (initial elements od dictionary in the end are also shown on the view).
    
    Returns:
    dict: A dictionary representing all cosmetics ever added to the project. 
    It contains product categories as keys and their respective lists as values.
    """

    for r in Rdz.rdz_list():
            
            v = Kosmetyk.kosmetyk_list(r)
            
            if v != []:
                d[r] = v
            
    return d
class produkty_views(View):
     
    def pindex(request, info= None):
        zmienna = zmienna_ustal()
        zmienna["form"] = RdzForm()
        zmienna["info"] = info

        return render(request,"produkty/indexcopy.html", zmienna)
    
    def addk_view(request):
         pass
                   



def wydziel(x):
    
        """
        Extracts the last element from a comma-separated string.
        
        This function takes a comma-separated string (string representation of cosmetics list "Marka, Nazwa" and extracts the last element, which is name (Nazwa).
        
        Parameters:
        x (str): The comma-separated string.
        
        Returns:
        str: The last element from the comma-separated string or a string itself (if no separator inside) - that is the cosmetic's name.
        """
    
        y = x.split(", ")
               
        return  y[-1]

   

            
def ustal_form(r):
        """
        Determines the appropriate form based on the given category.
    
        This function determines the appropriate form based on the given product category.
        
        Parameters:
        r (str): The product category.
    
        Returns:
        Form: An instance of the specific form based on the provided category.
        """
        form_mapping = {
            "Szampon": SzamponForm(),
            "Odżywka": OdżywkaForm(),
            "Maska": MaskaForm(),
            "Wcierka": WcierkaForm(),
            "Pianka": PiankaForm(),
            "Żel": ŻelForm(),
            "Krem": KremForm(),
            "Peeling": PeelingForm(),
            "Olej": OlejForm(),
            "Olejek": OlejekForm()
        }
        
        
    
        return form_mapping[r]
            



def obecnosc_ustal(r, n):
    
        """
        Determines if an object defined by the given name already exists in the database.
        
        This function determines if the product has already been added to the database based on the given product name.
        
        Parameters:
        r (str): The product category.
        n (str): The product name.
    
        Returns:
        True if product already exists in database and False if it is new.
        """
        
        n_mapping = {
              "Szampon": lambda n: True if Szampon.objects.get(Nazwa=n) else False,
               "Odżywka": lambda n: True if  Odżywka.objects.get(Nazwa=n) else False,
               "Maska":  lambda n: True if Maska.objects.get(Nazwa=n) else False,
               "Wcierka":  lambda n: True if Wcierka.objects.get(Nazwa=n) else False,
               "Pianka": lambda n: True if  Pianka.objects.get(Nazwa=n) else False,
               "Żel":  lambda n: True if Żel.objects.get(Nazwa=n) else False,
               "Krem":  lambda n: True if Krem.objects.get(Nazwa=n) else False,
               "Peeling": lambda n: True if  Peeling.objects.get(Nazwa=n) else False,
               "Olej":  lambda n: True if Olej.objects.get(Nazwa=n) else False,
               "Olejek":  lambda n: True if Olejek.objects.get(Nazwa=n) else False,
                }
            
        f=n_mapping[r]
        
        try:
            b=f(n)
        except:
            b=False
        return b


def index(request):
    
        """
         Handles the basic cosmetics collection view.
         
         
         This function shows the basic cosmetics collection view.
         It creates the variable r assigned to the session which represents the product category.
         It also allows authenticated users to start adding new product to the database based on session variable.
         
         Parameters:
         request (HttpRequest): The HTTP request object.
         
         Returns:
         HttpResponse: The HTTP response to be displayed.
         
         """
     
        if request.method == "POST":
            form=RdzForm(request.POST)
            if form.is_valid():
                r=request.POST["Rdz"]
                request.session["r"]= r
                
                 
                return render(request,"produkty/addk.html",{"form" : ustal_form(r)})
            else:
            
                info = "Upsss... coś poszło nie tak"
                return produkty_views.pindex(request, info) 

        else:
                   
            return produkty_views.pindex(request) 
                          
               

def addk(request): 
   
        """
        Handles adding new cosmetics to the database.
        
        
        This function  allows authenticated users to add the new cosmetic to database.
        It check if the session variable "r" exists within the session.
        Than the obecnosc_ustal() function is used to verify if the cosmetics has been already added.
        If given conditions are fulfilled the new cosmetic is added.
        
        Parameters:
        request (HttpRequest): The HTTP request object.
        
        Returns:
        HttpResponse: The HTTP response to be displayed.
        
        """
    
        if not request.user.is_authenticated:

            message = "Zaloguj się, aby dodać produkt do bazy"
            return  login_view(request, message)

        
        try: 
            "r" in request.session
            
        except:
            return produkty_views.pindex(request, "Error - brak rodzaju")          
         
        
        r = request.session["r"]
    
                
        if request.method == "POST":
            x = request.POST["Nazwa"]
            
            
            
            if obecnosc_ustal(r,x) == True:

                info =  f"Upsss... Ten kosmetyk ({x}) jest już w naszej bazie. Możesz zasilić nim swoją kosmetyczkę"

                return produkty_views.pindex(request, info)                 
               
                
            else:
                
                pass
           
            # try:
            #     print("a")
            #     obecnosc_ustal(r,x) == True
            #     print("b")
                                
            #     return render(request, "produkty/indexcopy.html", zmienna_ustal(
            #                   {
            #                     "form": RdzForm(),
            #                     "info": f"Upsss... Ten kosmetyk ({x}) jest już w naszej bazie. Możesz zasilić nim swoją kosmetyczkę"}))
                
            # except:
            #     print("false1")
                
            #     pass
            try:
            
                post_mapping = {
                    "Szampon": SzamponForm(request.POST),
                    "Odżywka": OdżywkaForm(request.POST),
                    "Maska": MaskaForm(request.POST),
                    "Wcierka": WcierkaForm(request.POST),
                    "Pianka": PiankaForm(request.POST),
                    "Żel": ŻelForm(request.POST),
                    "Krem": KremForm(request.POST),
                    "Peeling": PeelingForm(request.POST),
                    "Olej": OlejForm(request.POST),
                    "Olejek": OlejekForm(request.POST)
                }
                
                q = post_mapping[r]
                
            except:
            
                 return render(request,"produkty/addk.html", {
                     "form": ustal_form(request.session["r"]),
                     "info": "Upsss... coś poszło nie tak"})
                
            
                
            if q.is_valid():
               pass
         
            else: 
                 return render(request,"produkty/addk.html", {
                     "form": ustal_form(r),
                     "info": "Upsss... coś poszło nie tak"})
            
            k = q.save()
            k.set_Owner(request.user)
            k.save()
            workingsKosmetyk.set_work(k)
    
            info ="Baza zasilona" 
            return produkty_views.pindex(request, info) 
            
           
            
        else:
           
            return render(request,"produkty/add.html", {
                "form": ustal_form(r),
                "info": "nie ta metoda"
              })
        
def jeden(request, Nazwa):
    
        """
        Handles adding a product to the user's cosmetic collection.
    
        This function allows authenticated users to add a product to their cosmetic collection.
    
        Parameters:
        request (HttpRequest): The HTTP request object.
        Nazwa (str): The product name.
    
        Returns:
        HttpResponse: The HTTP response to be displayed (the view unique based on cosmetics name).
        """
        
        if not request.user.is_authenticated:
                return render(request, "users/login.html", {
                    "message" : "Zaloguj się, aby dodać produkt do swojej kosmetyczki"
                    })
        
        class Roboczy (forms.Form):
            N = forms.CharField(widget=forms.HiddenInput(), initial= Nazwa)
        
        
        if request.method=="POST":
            form=Roboczy(request.POST)
            if form.is_valid():
                nazwa = wydziel(request.POST["N"])
                Owner = request.user
                
                try:
                    Owner.wKosmetyczce.get(Nazwa=nazwa)                           
                except:
                        pass
                else:
                    mess =  "Sprawdź dokładniej, ten kosmetyk znajduje się już w Twojej koametyczce."
                    return wlosing_views.inform(request, mess)       
                    
                q = Kosmetyk.objects.get(Nazwa=nazwa)
                q.set_Owner(Owner)
   
                
                info = Włosy.get_info(Owner)
                kosmetyczka = Kosmetyk.get_kosmetyczka(Owner)
                

    
                mess =  "Gratulacje, Kosmetyczka zasilona!"
                return wlosing_views.inform(request, mess) 

        else:
            name = wydziel(Nazwa)
            name.capitalize()
            return render(request, "produkty/jeden.html", {
            "name": name,
            "form": Roboczy(),
           
          
            })
