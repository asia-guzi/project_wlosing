from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import Włosy #, Porowatość 

# Porowatość
from .forms import WłosyForm
from produkty.models import Kosmetyk

# Create your views here.

def get_info (owner, request):
    
        """
        Retrieves hair information for a given owner.
    
        This function retrieves hair information (length, color, porosity, and type) for the specified owner.
        
        Parameters:
        owner (str): The owner of the hair for whom the information is requested.
        request: The request object.
    
        Returns:
        str: A string containing hair information for the specified owner.
             If the owner has not provided basic hair information, a message prompting them to do so is returned.
        """
       
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
       """
        Handles the user account view.
        
        This function allows authenticated users to get and display user information regarding login, type of hair and cosmetica assigned.
        
        Parameters:
        request (HttpRequest): The HTTP request object.
        
        Returns:
        HttpResponse: The HTTP response to be displayed (depending on existance of hair and cosmetica information.)
        
        """
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

        
        """
         Handles assigning a hair object to the user's account.
         
         This function allows authenticated users to add a current type of their hair to the account.
         
         
         Parameters:
         request (HttpRequest): The HTTP request object.
         
         Returns:
         HttpResponse: The HTTP response to be displayed.
         
         """
        
        if not request.user.is_authenticated:
               return render(request, "users/login.html")
        
        if request.method == "POST":
            form  = WłosyForm(request.POST)
         
            if form.is_valid():
                name = request.user
                dl = request.POST["Długość"]
                ko = request.POST["Kolor"]
                po = request.POST["Porowatość"]
                ty = request.POST["Typ"]
                
                x = Włosy.objects.get(Długość=dl, Kolor=ko, Porowatość=po, Typ=ty)
                
                try:
                    y = Włosy.objects.get(Owner=name)
                    y.Owner.remove(name)
                    
                    
                except:
                   
                    pass
                    
                """ z tym cos nie tak """
            
                x.Owner.add(name)  
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
       
            
        
    
    
    
    