from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .forms import RdzForm, SzamponForm, OdżywkaForm, WcierkaForm, MaskaForm, PeelingForm, ŻelForm, PiankaForm, KremForm, OlejekForm, OlejForm #UzForm, 

from .models import Kosmetyk, Szampon, Odżywka, Wcierka, Maska, Peeling, Żel, Pianka, Krem, Olejek, Olej, Rdz
from django import forms
from wlosing.models import Włosy
from wlosing.views import get_info

 


def lista_ustal(r):

    try: 
        if r == "Szampon":
            x = Szampon.szampon_list()
        if r == "Odżywka":
            x =  Odżywka.odżywka_list()
        if r == "Maska":
            x =  Maska.maska_list()
        if r == "Wcierka":
            x =  Wcierka.wcierka_list()
        if r == "Pianka":
            x =  Pianka.pianka_list()
        if r == "Żel":
            x =  Żel.żel_list()
        if r == "Krem":
            x =  Krem.krem_list()
        if r == "Peeling":
            x =  Peeling.peeling_list()
        if r == "Olej":
            x =  Olej.peeling_list()
        if r == "Olejek":
            x =  Olejek.peeling_list()
    except:
        return []
      
    return x


def wydziel(x):
    
       y = x.split(", ")
       
       return  y[-1]

   
def zmienna_ustal(d):
    
        for r in Rdz.rdz_list():
             
                v = lista_ustal(r)
                
                if v != []:
                    d[r] = v
        return d
            
            

def ustal_form(r):
    if r == "Szampon":
        return SzamponForm()
    if r == "Odżywka":
        return OdżywkaForm()
    if r == "Maska":
        return MaskaForm()
    if r == "Wcierka":
        return WcierkaForm()
    if r == "Olejek":
        return OlejekForm()
    if r == "Olej":
        return OlejForm()
    if r == "Żel":
        return ŻelForm()
    if r == "Pianka":
        return PiankaForm()
    if r == "Krem":
        return KremForm()
    if r == "Peeling":
        return PeelingForm()


def obecnosc_ustal(r, n):
    if r == "Szampon":
        return Szampon.objects.get(Nazwa=n)
   
    if r == "Odżywka":
        return n in Odżywka.objects.get(Nazwa=n)
    if r == "Maska":
        return n in Maska.objects.get(Nazwa=n)
    if r == "Wcierka":
        return n in Wcierka.objects.get(Nazwa=n)
    if r == "Olejek":
        return n in Olejek.objects.get(Nazwa=n)
    if r == "Olej":
        return n in Olej.objects.get(Nazwa=n)
    if r == "Żel":
        return n in Żel.objects.get(Nazwa=n)
    if r == "Pianka":
        return n in Pianka.objects.get(Nazwa=n)
    if r == "Krem":
        return n in Krem.objects.get(Nazwa=n)
    if r == "Peeling":
        return n in Peeling.objects.get(Nazwa=n)


def index(request):
 
    if request.method == "POST":
        form=RdzForm(request.POST)
        if form.is_valid():
            r=request.POST["Rdz"]
            request.session["r"]= r
            
             
            return render(request,"produkty/addk.html",{"form" : ustal_form(r)})
        else:
        
            
            return render(request,"produkty/indexcopy.html", 
                zmienna_ustal( {
                "info": "Upsss... coś poszło nie tak",
                "form": RdzForm(),
                }))
                 
    else:
            
        varia = zmienna_ustal({"form" : RdzForm()})       
        return render(request, "produkty/indexcopy.html", varia )
                      
           

def addk(request): 
    
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {
            "message" : "Zaloguj się, aby dodać produkt do bazy"
            })
    
    try: 
        "r" in request.session
        
    except:
                  
        return render(request,"produkty/indexcopy.html", {
            "form": RdzForm(),
            "info": "Error - brak rodzaju"
            })
    
    r = request.session["r"]

            
    if request.method == "POST":
        x = request.POST["Nazwa"]
       
        try:
            obecnosc_ustal(r, x)
            
            return render(request, "produkty/indexcopy.html", {
                            "form": RdzForm(),
                            "info": f"Upsss... Ten kosmetyk ({x})jest już w naszej bazie. Możesz zasilić nim swoją kosmetyczkę"})
            
        except:
            pass
    
        
        if r == "Szampon":
            
            q = SzamponForm(request.POST)
                 
        elif r == "Odżywka":
            q = OdżywkaForm(request.POST)
           
        elif r == "Maska":
            q = MaskaForm(request.POST)
                    
        elif r == "Wcierka":
            q = WcierkaForm(request.POST)
           
        elif r == "Olejek":
            q =  OlejekForm(request.POST)
            
        elif r == "Olej":
            q =  OlejForm(request.POST)
             
        elif r == "Żel":
            q =  ŻelForm(request.POST)
            
        elif r == "Pianka":
            q =  PiankaForm(request.POST)
            
        elif r == "Krem":
            q =  KremForm(request.POST)
            
        elif r == "Peeling":
            q = PeelingForm(request.POST)
            
        else: 
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

        varia = zmienna_ustal({"form" : RdzForm(),"info" : "Baza zasilona", })
       
        return render(request, "produkty/indexcopy.html", varia )
       
            
        
    else:
       
        return render(request,"produkty/add.html", {
            "form": ustal_form(r),
            "info": "nie ta metoda"
          })
    
def jeden(request, Nazwa):
    
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
                info = get_info(Owner, request)
                kosmetyczka = Kosmetyk.objects.filter(Owner = Owner)
            
                return render(request, "wlosing/info.html", {
                    "message" : "Sprawdź dokładniej, ten kosmetyk znajduje się już w Twojej koametyczce.",
                    "name" : Owner,
                    "info" : info,
                    "kosmetyki" : kosmetyczka,
                    })
                           
            except:
                    pass
                    
                
            q = Kosmetyk.objects.get(Nazwa=nazwa)
            q.set_Owner(Owner)
            q.save()
            
            
            info = get_info(Owner, request)
            kosmetyczka = Kosmetyk.objects.filter(Owner = Owner)
            
            """tbc - zmiana wszedzie na x = Owner.wKosmetyczce.all()"""

                
        return render(request, "wlosing/info.html", {
            "message" : "Gratulacje, Kosmetyczka zasilona!",
            "name" : Owner,
            "info" : info,
            "kosmetyki" : kosmetyczka,
            })
        
    else:
        name = wydziel(Nazwa)
        name.capitalize()
        return render(request, "produkty/jeden.html", {
        "name": name,
        "form": Roboczy(),
      
        })
