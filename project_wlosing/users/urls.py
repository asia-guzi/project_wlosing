# -*- coding: utf-8 -*-

from django.urls import path
from . import views
from django.contrib import admin
  

app_name="users"



urlpatterns = [
    
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup, name="signup"),
]

