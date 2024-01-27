from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect

from produkty.models import Kosmetyk


# Create your views here.

def index(request):
    return render(request, "czytnik/index.html")


def tlumacz(request):
    return render(request, "czytnik/tlumacz.html")
