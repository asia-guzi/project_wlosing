import os
from django import setup

# Ustawienia środowiska Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_wlosing.settings")
setup()

# Importuj modele Django po skonfigurowaniu środowiska
from produkty.models import *
from wlosing.models import *





def main():
    input_wlosy()
    input_rodzaj()
    input_kosmetykin()


def input_kosmetykin():
        
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
    x = Odzywka.objects.create(marka="Anwen", nazwa="Proteinowa magnolia", PEH="Proteinowa")
    WorkingsKosmetyk.set_work(x)
    
 
def create_zel():
    x = Zel.objects.create(marka="Sysoss", nazwa="Power hold", hold="Mocny")
    WorkingsKosmetyk.set_work(x)


def create_pianka():
    x = Pianka.objects.create(marka="Wella", nazwa="Wellaflex", hold="Mocny")
    WorkingsKosmetyk.set_work(x)

    
def create_krem():
    x = Krem.objects.create(marka="Taft", nazwa="Curls", hold="Słaby")
    WorkingsKosmetyk.set_work(x)
    

def create_olejek():
    x = Olejek.objects.create(marka="Isana", nazwa="2in1 intensiv")
    WorkingsKosmetyk.set_work(x)


def create_wcierka():
    x = Wcierka.objects.create(marka="Anwen", nazwa="Grow Us Tender")
    WorkingsKosmetyk.set_work(x)


def create_peeling():
    x = Peeling.objects.create(marka="Bandi", nazwa="Tricho Esthetic Peeling")
    WorkingsKosmetyk.set_work(x)
           

def create_szampony():
    szampony = [
        ("Anwen", "Mint it Up!", "Średni"),
    ]

    for s in szampony:
        x, y, z = s
        a = Szampon.objects.create(marka=x, nazwa=y, moc=z)
        WorkingsKosmetyk.set_work(a)
        

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
        a = Maska.objects.create(marka=x, nazwa=y, PEH=z)
        WorkingsKosmetyk.set_work(a)
        
        
def create_oleje():
    oleje = [
        ("OnlyBio", "Z pestek winogron"),
        ("Anwen", "Konopny")
    ]

    for o in oleje: 
        x, y = o
        a = Olej.objects.create(marka=x, nazwa=y)
        WorkingsKosmetyk.set_work(a)


def input_rodzaj():
    
    for r in ["Szampon", "Odzywka", "Maska", "Olejek", "Olej", "Wcierka", "Zel", "Pianka", "Krem", "Peeling"]:
        Rdz.objects.create(rodzaj=r)


def input_wlosy():
    
    dlugosc_choices = [
        "Krótkie",
        "Średnie",
        "Długie",
        ]

    kolor_choices = [
        "Blond",
        "Szatynka", 
        "Brunetka", 
        "Rude", 
        ]
    porowatosc_choices = [
        "Wysokoporowate", 
        "Średnioporowate", 
        "Niskoporowate", 
        ]
    typ_choices = [
        "Proste",
        "Falowane",
        "Wurly",
        "Kręcone",
        "Afro",
        ]

    for x in dlugosc_choices:
        for y in kolor_choices:
            for z in porowatosc_choices:
                for q in typ_choices:
                    i = Wlosy.objects.create()
                    i.set_all(x, y, z, q)
                    i.save()


if __name__ == "__main__":
    main()
