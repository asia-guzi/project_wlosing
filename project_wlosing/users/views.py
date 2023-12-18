from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.contrib.auth.models import User
from wlosing.models import Włosy

# Create your views here.



def check_password(password):
    
    """
    Validates a password based on specified criteria.

    This function validates a password based on the following criteria:
    - The password must be at least 8 characters long.
    - The password must contain both uppercase and lowercase characters.
    - The password must contain at least one numeric digit.

    Parameters:
    password (str): The password to be validated.

    Returns:
    bool: True if the password meets the criteria, False otherwise.
    """
    
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
    
    """
Validates an email address based on specified criteria.

This function validates an email address based on the following criteria:
- The email must contain "@" and "." symbols.
- There must be at least two characters after the last "." symbol and at most three characters.
- The "@" symbol must appear before the last "." symbol.

Parameters:
mail (str): The email address to be validated.

Returns:
bool: True if the email address meets the criteria, False otherwise.
"""
    
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
    
    
def login_view(request, message = None):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('wlosing:info')) 
        else:
            message =  "Niewłaściwy login lub hasło."
            
    
    if message:
        return render(request, "users/login.html", {"message":message})
    else:
        return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "wlosing/index.html", {
        "message": "Wylogowano."
    })    
    
def signup (request):
    
    """
Handles user sign-up process.

This function handles the user sign-up process:
- Retrieves user details from the request (username, password, email).
- Checks if the username and email are not already in use.
- Validates the email using the check_email function.
- Validates the password using the check_password function.
- Creates a new user using the User model.
- Logs in the new user.

Parameters:
request: The request object containing user details.

Returns:
HttpResponseRedirect: Redirects to the "quest" page upon successful sign-up.
"""
    
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
   
    
