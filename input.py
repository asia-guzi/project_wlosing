
def main():
    input_wlosy()
    input_rodzaj()
    input_kosmetyki()


def input_kosmetyki():

        
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
    Odżywka.objects.create(Marka="Anwen", Nazwa="Proteinowa magnolia", PEH="Proteinowa")
    
 
def create_zel(Marka="Sysoss", Nazwa="Power hold", Hold="Mocny"):
    Żel.objects.create(Marka="Sysoss", Nazwa="Power hold", Hold="Mocny")

    
def create_pianka(Marka="Wella", Nazwa="Wellaflex", Hold="Mocny"):
    Pianka.objects.create(Marka="Wella", Nazwa="Wellaflex", Hold="Mocny")

    
def create_krem(Marka="Taft", Nazwa="Curls", Hold="Słaby"):
    Krem.objects.create(Marka="Taft", Nazwa="Curls", Hold="Słaby")
    
def create_olejek(Marka="Isana", Nazwa="2in1 intensiv"):
    Olejek.objects.create(Marka="Isana", Nazwa="2in1 intensiv")

def create_wcierka(Marka="Anwen", Nazwa="Grow Us Tender"):
    Wcierka.objects.create(Marka="Anwen", Nazwa="Grow Us Tender")

def create_peeling():
    Peeling.objects.create(Marka="Bandi", Nazwa="Tricho Esthetic Peeling")
           
def create_szampony(self):
    szampony = [
    ("Anwen","Mint it Up!", "Średni"),
    ]
    

    for s in szampony:
        x, y, z = s
        Szampon.objects.create(Marka=x, Nazwa=y, Moc=z)
        
def create_maski(self):
    maski = [
        ("Garnier Hairfood", "Kakao", "Emolientowa"),
        ("Yope", "Mleko owsiane", "PEH"),
        ("Yope", "Orientalny ogród", "PEH"),
        ("Anwen", "Proteinowa magnolia", "Proteinowa"),
        ("OnlyBio", "Maska do włosów niskoporowatych", "PEH"),
        ]    

        
    for m in maski:
        x, y, z = m
        Maska.objects.create(Marka=x, Nazwa=y, PEH=z)
        
        
def create_oleje(self):
    oleje = [
    ("OnlyBio", "Z pestek winogron"),
    ("Anwen", "Konopny")
    ]
    
    for o in oleje: 
        x,y = o
        Olej.objects.create(Marka=x, Nazwa=y)   
        

   
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