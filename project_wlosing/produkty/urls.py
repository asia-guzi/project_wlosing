# -*- coding: utf-8 -*-
from django.urls import path
from . import views

app_name = "produkty"

urlpatterns = [
    path("", views.index, name="index"),
    path("addk", views.addk, name="addk"),
    path("<str:nazwa>", views.jeden, name="jeden")
    ]
