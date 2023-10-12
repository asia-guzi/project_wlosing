# -*- coding: utf-8 -*-
from django.urls import path
from . import views

app_name="czytnik"

urlpatterns = [
    path("", views.index, name="index"),
    path("tlumacz", views.tlumacz, name="tlumacz"),
    
    
    ]