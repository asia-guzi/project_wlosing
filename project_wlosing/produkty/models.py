from django.db import models
from project_wlosing import settings


         
            
class Rdz (models.Model):
                       
            Rdz = models.CharField(max_length=300, unique=True)
            #""" input:
                # for q in ["Szampon", "Odżywka", "Maska", "Olejek", "Olej", "Wcierka", "Żel", "Pianka", "Krem", "Peeling"]:
                # k = Rdz ()
                # k.set_Rdz(q)
                # k.save() """
            
            
                
            def set_Rdz (self, rdz):
                self.Rdz = rdz
            def get_Rdz (self):
                return self.Rdz
            
            def __str__(self):
                 return f"{self.Rdz} "
            
            def rdz_list(): 
                return  ["Szampon", "Odżywka", "Maska", "Olejek", "Olej", "Wcierka", "Żel", "Pianka", "Krem", "Peeling"]
            
            
class Kosmetyk (models.Model):
         
            Marka = models.CharField(max_length=300)
            Nazwa = models.CharField(max_length=300)
            Owner = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="wKosmetyczce", blank = True)
             
            
            def get_Rodzaj (self):
                return self.Rodzaj
            def get_Marka (self):
                return self.Marka
            def get_Nazwa (self):
                return self.Nazwa
            def get_Owner (self):
                return self.Owner
            

            def set_Marka (self, m):
                self.Marka = m
            def set_Nazwa (self, n):
                self.Nazwa = n
            def set_Owner (self, o):
                self.Owner.add(o)
           
                            
            def __str__(self):
                 return f"{self.Marka}, {self.Nazwa} "
             
            def kosmetyk_list():
                    """"TBC czy tutaj sie nie da bezposrednio skorzystac z queryset?
                     + do przemylenia: jedna funkcja list dla wszystkich kosmetykow"""
                    k = Kosmetyk.objects.all()
                    L=[]
                    for x in k:
                                    
                        m = x.get_Marka()
                        n = x.get_Nazwa()
                        L.append((m,n))
                    return L
                
                
               # def get_skład(self, name):
                   #     """wsywietla skład kosmetyku który jest w bazie"""
        #     try: 
        #         x = Skład.objects.get(name=name)
                
        #     except: return "Error"
                
        #     inci = x.INCI
        #     pl = x.PL
        # #     return ( inci, pl)
        
    
            # def get_skład(self):
            #     return self.Skład #lub skorzysta z related name
   
            

class Szampon (Kosmetyk):
    
        

    MOC_CHOICES = [
    ( "Łagodny", "Łagodny"), 
    ("Średni","Średni"), 
    ("Rypacz (mocny)", "Rypacz (mocny)"), 
    ]

    Rodzaj = models.ForeignKey(Rdz, to_field = "Rdz",  on_delete=models.CASCADE, related_name="Szampony", default = "Szampon")
    Moc = models.CharField ( max_length=300, choices = MOC_CHOICES)

    def get_Moc (self):
        return self.Moc
    

    def set_Moc (self, m):
        self.Moc = m
 
    
 
    def szampon_list():
            k = Szampon.objects.all()
            L=[]
            for x in k:
                            
                m = x.get_Marka()
                n = x.get_Nazwa()
                L.append(f"{m}, {n}")
            return L     

    
class O_M (Kosmetyk):
    
    PEH_CHOICES={
        ("Emolientowa", "Emolientowa"),
        ("Proteinowa", "Proteinowa"),
        ("Humektantowa","Humektantowa"),
        ("PEH'owa", "PEH"),
        ("Emolientowo - humektantowa", "EH"),
        ("Humektantowo - emolientowa", "HE"),
        
        }
    PEH = models.CharField(max_length=300, choices = PEH_CHOICES)
    
    def get_PEH (self):
        return self.Owner
    

    def set_PEH (self, m):
        self.PEH = m
        
    def set_all(self, rdz, m, n, o, p):
        self.set_Rodzaj(rdz)
        self.set_Marka( m)
        self.set_Nazwa(n )
        self.set_PEH(p)
        
    class Meta:
            abstract = True
            

    
    
class Odżywka (O_M):
 

    Rodzaj = models.ForeignKey(Rdz, to_field = "Rdz", on_delete=models.CASCADE, related_name="Odżywki",  default="Odżywka")

     
    def odzywka_list():
            k = Odżywka.objects.all()
            L=[]
            for x in k:
                            
                m = x.get_Marka()
                n = x.get_Nazwa()
                L.append(f"{m}, {n}")
            return L   
     
class Maska (O_M):
        
    Rodzaj = models.ForeignKey(Rdz, to_field = "Rdz", on_delete=models.CASCADE, related_name="Maski", default="Maska")


    def maska_list():
            k = Maska.objects.all()
            L=[]
            for x in k:
                            
                m = x.get_Marka()
                n = x.get_Nazwa()
                L.append(f"{m}, {n}")
            return L   

class Stylizator (Kosmetyk):
    HOLD_CHOICES = [
    ( "Lekki", "Lekki"), 
    ("Średni","Średni"), 
    ("Mocny", "Mocny"), 
    ]

    Hold = models.CharField ( max_length=300, choices = HOLD_CHOICES)
    
    def set_all(self, rdz, m, n, o, s):
        self.set_Rodzaj(rdz)
        self.set_Marka( m)
        self.set_Nazwa(n )
        self.set_Hold(s)
    
    def get_Hold (self):
        return self.Owner
    

    def set_Hold (self, m):
        self.Hold = m
        
        

    
class Żel (Stylizator):
    
    Rodzaj = models.ForeignKey(Rdz, to_field = "Rdz",  on_delete=models.CASCADE, related_name="Żele",   default="Żel")


    def żel_list():
            k = Żel.objects.all()
            L=[]
            for x in k:
                            
                m = x.get_Marka()
                n = x.get_Nazwa()
                L.append(f"{m}, {n}")
            return L   
     
class Pianka (Stylizator):
    
    Rodzaj = models.ForeignKey(Rdz, to_field = "Rdz", on_delete=models.CASCADE, related_name="Pianki",  default="Pianka")

     
    def pianka_list():
            k = Pianka.objects.all()
            L=[]
            for x in k:
                            
                m = x.get_Marka()
                n = x.get_Nazwa()
                L.append(f"{m}, {n}")
            return L      
     
class Krem (Stylizator):
    
   
    Rodzaj = models.ForeignKey(Rdz, to_field = "Rdz",  on_delete=models.CASCADE, related_name="Kremy",  default="Krem")


    def krem_list():
            k = Krem.objects.all()
            L=[]
            for x in k:
                            
                m = x.get_Marka()
                n = x.get_Nazwa()
                L.append(f"{m}, {n}")
            return L   

class Olej (Kosmetyk):
    
    Rodzaj = models.ForeignKey(Rdz, to_field = "Rdz", on_delete=models.CASCADE, related_name="Oleje",  default="Olej")

    def olej_list():
            k = Olej.objects.all()
            L=[]
            for x in k:
                            
                m = x.get_Marka()
                n = x.get_Nazwa()
                L.append(f"{m}, {n}")
            return L   
        
     
     
class Olejek (Kosmetyk):
    
    Rodzaj = models.ForeignKey(Rdz, to_field = "Rdz", on_delete=models.CASCADE, related_name="Olejki",   default="Olejek")

    def olejek_list():
            k = Olejek.objects.all()
            L=[]
            for x in k:
                            
                m = x.get_Marka()
                n = x.get_Nazwa()
                L.append(f"{m}, {n}")
            return L   
     
class Wcierka (Kosmetyk):
    
    Rodzaj = models.ForeignKey(Rdz, to_field = "Rdz", on_delete=models.CASCADE, related_name="Wcierki",   default="Wcierka")

    def wcierka_list():            
            k = Wcierka.objects.all()
            L=[]
            for x in k:
                            
                m = x.get_Marka()
                n = x.get_Nazwa()
                L.append(f"{m}, {n}")
            return L   
     
class Peeling (Kosmetyk):
    
    Rodzaj = models.ForeignKey(Rdz, to_field = "Rdz", on_delete=models.CASCADE, related_name="Peelingi",   default="Peeling")
    def peeling_list():
            k = Peeling.objects.all()
            L=[]
            for x in k:
                            
                m = x.get_Marka()
                n = x.get_Nazwa()
                L.append(f"{m}, {n}")
            return L   




        
      
            
    
        
        

   
    
  