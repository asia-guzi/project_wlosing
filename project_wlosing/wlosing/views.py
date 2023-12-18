from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import Włosy #, Porowatość 
from django.views import View

# Porowatość
from .forms import WłosyForm
from produkty.models import Kosmetyk



class wlosing_views(View):
     
    def inform(request, message = None):
       """
        Handles the user account view.
        
        This function allows authenticated users to get and display user information regarding login, type of hair and cosmetica assigned.
        
        Parameters:
        request (HttpRequest): The HTTP request object.
        
        Returns:
        HttpResponse: The HTTP response to be displayed (depending on existance of hair and cosmetics information.)
        
        """
       if not request.user.is_authenticated:
           return render(request, "users/login.html")
      
       Owner = request.user
       info, check_w = Włosy.get_info(Owner, True)    
       kosmetyczka, check_k = Kosmetyk.get_kosmetyczka(Owner, True)
       input_info={"name" : Owner}

       if check_w == True:
            input_info["opcja"] = info
       else:
            input_info["info"] = info
       if check_k == True:
            input_info["kosmetyki"] = kosmetyczka
       if message:
            input_info["message"] = message


       return render(request, "wlosing/info.html", input_info)





def index(request):
    return render(request, "wlosing/index.html")

def info(request):
      return wlosing_views.inform(request)

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
               
                x.Owner.add(name)  
                info = Włosy.get_info(name)
                return render (request, "wlosing/info.html", {
                    "name" : name ,
                    "info" : info,
                    "kosmetyki" : Kosmetyk.get_kosmetyczka(name)
                    })
    
       
 
        return render(request, "wlosing/quest.html", {
            "form": WłosyForm()
        })
       
            
        
    
    
    
    