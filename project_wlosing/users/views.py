from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.contrib.auth.models import User
from wlosing.models import Włosy

# Create your views here.



def check_password(password):
    le = len(password)
    
    try: 
        le >= 8
        
    except: 
        return False
    
    if password.islower() == True :
        return False
      
    for p in password:
       
        W = True
        try: 
            int(p)
            break
            
        except:
            W = False
        
    if W == True:
            return True
    else:       
        return False
        
  

def check_email(mail):
    
    try:
        
        a = mail.index("@")        
        b = mail.rindex(".")
        c = len(mail)-b-1
          
    except:
        return False
          
    if c>= 2 and c<=3:
     
       pass
         
    else:
        return False
    
    if a<b:
       
        return True
    
    else:
        return False
    
    
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            return HttpResponseRedirect(reverse('wlosing:info'))
        
        else:
            return render(request, "users/login.html", {
                "message": "Niewłaściwy login lub hasło."
            })
    else:
        return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "wlosing/index.html", {
        "message": "Wylogowano."
    })    
    
def signup (request):
    if request.method=="POST":
        name = request.POST['username']
        password = request.POST["password"]
        mail = request.POST['email']
       
        try:
            user = User.objects.get(username=name)
            return render(request, "users/signup.html", {
                "error" : f"Podany login {name} jest już zajęty, wprowadź nowy login" })
        except User.DoesNotExist:
            pass
        
               
        try:
            User.objects.get(email=mail)
            return render(request, "users/signup.html", {
                "error" : "Upss, istnieje już konto związane z podanym adresem email. Spróbuj się na nie zalogować" })
        except:
            pass
        
        if check_email(mail)== True:
            pass
        
        else:
            return render(request, "users/signup.html", {
                "error" : "Upss, wpisz poprawny adres email" })
        
        if check_password(password)== True:
            pass
        else :
            return render(request, "users/signup.html", {
                "error" : "Hasło musi zawierać conajmniej 8 znaków, w tym jedną wielką literę oraz cyfrę"})
        
        try:
            request.POST['password'] == request.POST['password1']
        except :
            return render(request, "users/signup.html", {
                "error" : "Podane hasła różnią się od siebie."}) 
        
        
        user = User.objects.create_user(request.POST['username'], request.POST['email'],  request.POST['password'])
        user.save()
        auth.login(request, user)
        return HttpResponseRedirect(reverse("wlosing:quest"))
                                               
    else:
        return render(request, "users/signup.html")
   
    
