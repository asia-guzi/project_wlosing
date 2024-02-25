from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.


def check_password(password: str) -> bool:
    """
    Validates a password based on specified criteria.

    This function validates a password based on the following criteria:
    - The password must be at least 8 characters long.
    - The password must contain both uppercase and lowercase characters.
    - The password must contain at least one numeric digit.

    :param password: The password to be validated.
    :type password: str

    :return: True if the password meets the criteria, False otherwise.
    :rtype: bool
    """
    # check if length of password is valid
    le = len(password)
    if le >= 8:
        pass
    else:
        return False
    
    # check if any letter is uppercase
    if password.islower():
        return False
    
    # check if there is any integer within the password
    for p in password:       
        try: 
            int(p)  
        except ValueError:
            pass
        else:
            return True
    return False


def check_email(mail: str) -> bool:
    """
    Validates an email address based on specified criteria.

    This function validates an email address based on the following criteria:
    - The email must contain "@" and "." symbols.
    - There must be at least two characters after the last "." symbol and at most three characters.
    - The "@" symbol must appear before the last "." symbol.

    :param mail: The email address to be validated.
    :type mail: str

    :return: True if the email address meets the criteria, False otherwise.
    :rtype: bool
    """

    # check if . and @ in e-mail
    try:
        a = mail.index("@")        
        b = mail.rindex(".")
        c = len(mail)-b-1
    except ValueError:
        return False

    # check if at least two characters after the last "." symbol and at most three
    if 2 <= c <= 3:
        pass
    else:
        return False

    # checks if @ before .
    if a < b:
        return True
    
    else:
        return False
    
    
def login_view(request: HttpRequest, message: str = None) -> HttpResponse:
    """
    Handles the login page view.

    This function renders the login page and handles user login attempts.
    If `message` is provided, it displays a message to the user, such as an error message.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :param message: Optional message to be displayed on the login page (default is None).
    :type message: str, optional

    :return: The HTTP response displaying the login page.
    :rtype: HttpResponse
    """

    # authentication
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('wlosing:info')) 
        else:
            message = "Niewłaściwy login lub hasło."

    if message:
        return render(request, "users/login.html", {"message": message})
    else:
        return render(request, "users/login.html")


def logout_view(request: HttpRequest) -> HttpResponse:
    """
    Handles the logout page view.

    This function logs out the current user and redirects them to the home page.

    :param request: The HTTP request object.
    :type request: HttpRequest

    :return: The HTTP response redirecting the user to the home page.
    :rtype: HttpResponse
    """
    logout(request)
    return render(request, "wlosing/index.html", {
        "message": "Wylogowano."
    })    
    

def signup(request: HttpRequest) -> HttpResponseRedirect:
    """
    Handles user sign-up process.

    This function handles the user sign-up process:
    - Retrieves user details from the request (username, password, email).
    - Checks if the username and email are not already in use.
    - Validates the email using the check_email function.
    - Validates the password using the check_password function.
    - Creates a new user using the User model.
    - Logs in the new user.

    :param request: The HTTP request object containing user details.
    :type request: HttpRequest

    :return: Redirects to the "quest" page upon successful sign-up.
    :rtype: HttpResponseRedirect
    """

    # get data
    if request.method == "POST":
        name = request.POST['username']
        password = request.POST["password"]
        mail = request.POST['email']
       
        # check if the username / email is already in the base
        try:
            User.objects.get(username=name)
        except User.DoesNotExist:
            pass
        else:
            return render(request, "users/signup.html", {
                "error": f"Podany login {name} jest już zajęty, wprowadź nowy login"})

# tu możnaby pokombinować też z raise
        try:
            User.objects.get(email=mail)
        except User.DoesNotExist:
            pass
        else:
            return render(request, "users/signup.html", {
                "error": "Upss, istnieje już konto związane z podanym adresem email. Spróbuj się na nie zalogować"})

        # checks if e-mail meets the criteria
        if check_email(mail):
            pass
        else:
            return render(request, "users/signup.html", {
                "error": "Upss, wpisz poprawny adres email"})

        # checks if password meets the criteria
        if check_password(password):
            pass
        else:
            return render(request, "users/signup.html", {
                "error": "Hasło musi zawierać conajmniej 8 znaków, w tym jedną wielką literę oraz cyfrę"})
        
        if request.POST['password'] == request.POST['password1']:
            pass
        else:
            return render(request, "users/signup.html", {
                "error": "Podane hasła różnią się od siebie."})
        
        # create user account
        user = User.objects.create_user(request.POST['username'], request.POST['email'],  request.POST['password'])
        user.save()
        auth.login(request, user)
        return HttpResponseRedirect(reverse("wlosing:quest"))
                                               
    else:
        return render(request, "users/signup.html")
