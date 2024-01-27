import os
from django import setup

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_wlosing.settings")
setup()

from produkty.models import *
from wlosing.models import Włosy

def main():
    input_wlosy()
    input_rodzaj()
    input_kosmetykinWK()


def input_kosmetykinWK():

        
        create_maski()
        create_oleje()
        create_szampony()
        create_peeling()
        create_wcierka()
        create_olejek()
        create_krem()
        create_pianka()
        create_zel()
        create_odzywka()

 
 
def create_odzywka():
    x = Odżywka.objects.create(Marka="Anwen", Nazwa="Proteinowa magnolia", PEH="Proteinowa")
    workingsKosmetyk.set_work(x)
    
 
def create_zel(Marka="Sysoss", Nazwa="Power hold", Hold="Mocny"):
    x = Żel.objects.create(Marka="Sysoss", Nazwa="Power hold", Hold="Mocny")
    workingsKosmetyk.set_work(x)


    
def create_pianka(Marka="Wella", Nazwa="Wellaflex", Hold="Mocny"):
    x = Pianka.objects.create(Marka="Wella", Nazwa="Wellaflex", Hold="Mocny")
    workingsKosmetyk.set_work(x)

    
def create_krem(Marka="Taft", Nazwa="Curls", Hold="Słaby"):
    x = Krem.objects.create(Marka="Taft", Nazwa="Curls", Hold="Słaby")
    workingsKosmetyk.set_work(x)
    
def create_olejek(Marka="Isana", Nazwa="2in1 intensiv"):
    x = Olejek.objects.create(Marka="Isana", Nazwa="2in1 intensiv")
    workingsKosmetyk.set_work(x)

def create_wcierka(Marka="Anwen", Nazwa="Grow Us Tender"):
    x = Wcierka.objects.create(Marka="Anwen", Nazwa="Grow Us Tender")
    workingsKosmetyk.set_work(x)

def create_peeling():
    x = Peeling.objects.create(Marka="Bandi", Nazwa="Tricho Esthetic Peeling")
    workingsKosmetyk.set_work(x)
           
def create_szampony():
    szampony = [
    ("Anwen","Mint it Up!", "Średni"),
    ]
    

    for s in szampony:
        x, y, z = s
        a = Szampon.objects.create(Marka=x, Nazwa=y, Moc=z)
        workingsKosmetyk.set_work(a)
        
def create_maski():
    maski = [
        ("Garnier Hairfood", "Kakao", "Emolientowa"),
        ("Yope", "Mleko owsiane", "PEH"),
        ("Yope", "Orientalny ogród", "PEH"),
        ("Anwen", "Proteinowa magnolia", "Proteinowa"),
        ("OnlyBio", "Maska do włosów niskoporowatych", "PEH"),
        ]    

        
    for m in maski:
        x, y, z = m
        a = Maska.objects.create(Marka=x, Nazwa=y, PEH=z)
        workingsKosmetyk.set_work(a)
        
        
def create_oleje():
    oleje = [
    ("OnlyBio", "Z pestek winogron"),
    ("Anwen", "Konopny")
    ]

    for o in oleje: 
        x,y = o
        a = Olej.objects.create(Marka=x, Nazwa=y)   
        workingsKosmetyk.set_work(a)
        


def input_rodzaj():
    
    
    for r in ["Szampon", "Odżywka", "Maska", "Olejek", "Olej", "Wcierka", "Żel", "Pianka", "Krem", "Peeling"]:
        Rdz.objects.create(Rodzaj=r)  

def input_wlosy():
    
    DŁUGOŚĆ_CHOICES = [
        "Krótkie",
        "Średnie",
        "Długie",
        ]

    KOLOR_CHOICES = [
        "Blond",
        "Szatynka", 
        "Brunetka", 
        "Rude", 
        ]
    POROWATOŚĆ_CHOICES = [
        "Wysokoporowate", 
        "Średnioporowate", 
        "Niskoporowate", 
        ]
    TYP_CHOICES = [
        "Proste",
        "Falowane",
        "Wurly",
        "Kręcone",
        "Afro",
        ]

    for x in DŁUGOŚĆ_CHOICES:
        for y in KOLOR_CHOICES:
            for z in POROWATOŚĆ_CHOICES:
                for q in TYP_CHOICES:
                    i = Włosy.objects.create()
                    i.set_all(x,y,z,q)
                    i.save()





if __name__ == "__main__":
    main()