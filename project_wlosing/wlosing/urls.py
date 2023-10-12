
from django.urls import path
from . import views
# -*- coding: utf-8 -*-

app_name="wlosing"

urlpatterns= [
    path("", views.index, name="index"),
    path("info", views.info, name="info"),
    path("quest", views.quest, name="quest"),
    
    ]
