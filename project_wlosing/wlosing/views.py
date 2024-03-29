from django.shortcuts import render
from .models import Wlosy   # porowatosc
from django.views import View
from django.http import HttpResponse, HttpRequest

# porowatosc
from .forms import WlosyForm
from produkty.models import Kosmetyk


class WlosingViews(View):

    @staticmethod
    def inform(request: HttpRequest, mess: str = None) -> HttpResponse:
        """
        Handles the user account view.

        This function allows authenticated users to retrieve and display user information
        related to login, type of hair, and assigned cosmetics.

        :param request: The HTTP request object.
        :type request: HttpRequest
        :param mess: Additional message (default is None).
        :type mess: str, optional

        :return: The HTTP response to be displayed, rendering the "wlosing/info.html" template with
                 the provided input_info dictionary if available. If `mess` is provided, it will
                 also be included in the context passed to the template.
        :rtype: HttpResponse
        """

        # check authentication
        if not request.user.is_authenticated:
            return render(request, "users/login.html")
      
        owner = request.user

        # get hair info
        inf, check_w = Wlosy.get_info(owner, True)
        kosmetyczka, check_k = Kosmetyk.get_kosmetyczka(user=owner, check=True)
        print(kosmetyczka)

        # get context for the view
        input_info = {"name": owner}

        if check_w:
            input_info["opcja"] = info
        else:
            input_info["info"] = info
        if check_k:
            input_info["kosmetyki"] = kosmetyczka
        if mess:
            input_info["message"] = mess

        input_info["info"] = inf

        if check_k:
            print(check_k, 'checkk')
            input_info["kosmetyki"] = kosmetyczka

        if mess:
            input_info["message"] = mess
        print(input_info)

        return render(request, "wlosing/info.html", input_info)


def index(request: HttpRequest) -> HttpResponse:
    """
    Renders the homepage of the website.

    :param request: The HTTP request object.
    :type request: HttpRequest

    :return: The HTTP response displaying the homepage.
    :rtype: HttpResponse
    """
    return render(request, "wlosing/index.html")


def info(request: HttpRequest) -> HttpResponse:
    """
    Displays user information page.

    :param request: The HTTP request object.
    :type request: HttpRequest

    :return: The HTTP response generated by the 'inform' view function from 'WlosingViews'.
    :rtype: HttpResponse
    """
    return WlosingViews.inform(request)


def quest(request: HttpRequest) -> HttpResponse:

    """
    Handles the assignment of a hair object to the user's account.

    This function allows authenticated users to add the current type of their hair to their account.

    :param request: The HTTP request object.
    :type request: HttpRequest

    :return: The HTTP response to be displayed.
    :rtype: HttpResponse
    """

    # user authentication
    if not request.user.is_authenticated:
        return render(request, "users/login.html")

    if request.method == "POST":
        form = WlosyForm(request.POST)

        # get hair data
        if form.is_valid():
            name = request.user

            dl = request.POST["dlugosc"]
            ko = request.POST["kolor"]
            po = request.POST["porowatosc"]
            ty = request.POST["typ"]

            x = Wlosy.objects.get(dlugosc=dl, kolor=ko, porowatosc=po, typ=ty)

            # remove old hair type if any
            try:
                y = Wlosy.objects.get(owner=name)
                y.owner.remove(name)
            except Wlosy.DoesNotExist:
                pass
            except ValueError:
                pass

            # assign specific hare to the user's account
            x.owner.add(name)

            return WlosingViews.inform(request)

    return render(request, "wlosing/quest.html", {
        "form": WlosyForm()
    })
