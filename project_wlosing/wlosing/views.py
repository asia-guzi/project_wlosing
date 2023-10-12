from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import Włosy #, Porowatość 

# Porowatość
from .forms import WłosyForm
from produkty.models import Kosmetyk

# Create your views here.

def get_info (owner, request):
        
        try: 
            x = Włosy.objects.get(Owner=owner)
            
        except: 
            
            return "Upss... Nie uzupełniłaś podstawowych informacji o swoich włosach! Dodaj je aby móc w pełnin korzystać ze strony:"
            
        Długość = x.get_Długość()
        Kolor = x.get_Kolor()
        Porowatość = x.get_Porowatość()
        Typ = x.get_Typ()
                         
        return f"Masz {Długość}, {Kolor}, {Porowatość}, {Typ} włosy."

def index(request):
    return render(request, "wlosing/index.html")

def info(request):
       if not request.user.is_authenticated:
           return render(request, "users/login.html")
      
       Owner = request.user
       info = get_info(Owner, request)
       kosmetyczka = Kosmetyk.objects.filter(Owner = Owner)
       
       if info == "Upss... Nie uzupełniłaś podstawowych informacji o swoich włosach! Dodaj je aby móc w pełnin korzystać ze strony:":
           return render(request, "wlosing/info.html", {
               "name" : Owner,
               "opcja": info,
               "kosmetyki" : kosmetyczka
               }) 
               
       else:
              
           return render(request, "wlosing/info.html", {
               "name" : Owner,
               "info" : info,
               "kosmetyki" : kosmetyczka
               }) 

def quest (request):
    
    if not request.user.is_authenticated:
           return render(request, "users/login.html")
    
    if request.method == "POST":
        form  = WłosyForm(request.POST)
     
        if form.is_valid():
            name = request.user
            
            try:
                x = Włosy.objects.get(Owner = name)
                x.Długość = request.POST["Długość"]
                x.Kolor = request.POST["Kolor"]
                x.Porowatość = request.POST["Porowatość"]
                x.Typ= request.POST["Typ"]
                
            except:
                
                x = form.save(commit=False)
                x.Owner = request.user
                
                
                
            x.save()    
            info = get_info(name, request)
            return render (request, "wlosing/info.html", {
                "name" : name ,
                "info" : info,
                "kosmetyki" : Kosmetyk.objects.filter(Owner = request.user),
                
                })

   
    else:
        return render(request, "wlosing/quest.html", {
            "form": WłosyForm()
        })
   
        
    
    
    
    
    