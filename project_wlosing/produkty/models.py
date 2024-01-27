from django.db import models
from project_wlosing import settings
from django.contrib.auth.models import User
from typing import Type, Tuple
from django.db.models.query import QuerySet
from django.contrib.auth.models import User



         
            
class Rdz (models.Model):
                       
            Rodzaj = models.CharField(max_length=300, unique=True)
               
            def set_Rodzaj (self, rdz):
                self.Rodzaj= rdz
            def get_Rodzaj(self):
                return self.Rodzaj
            
            def __str__(self):
                 return f"{self.Rodzaj}"
            
            def rdz_list(cls): 
                return  [r.Rodzaj for r in cls.all()]
class Kosmetyk (models.Model):
            Marka = models.CharField(max_length=300)
            Nazwa = models.CharField(max_length=300)
            Owner = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="wKosmetyczce", blank = True)
          
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
             
            def kosmetyk_map(cls, r):
                 mapping = {
                            "Szampon": Szampon,
                            "Odżywka": Odżywka,
                            "Maska": Maska,
                            "Wcierka": Wcierka,
                            "Pianka": Pianka,
                            "Żel": Żel,
                            "Krem": Krem,
                            "Peeling": Peeling,
                            "Olej": Olej,
                            "Olejek": Olejek,
                        }  
                 return mapping[r]   
            def kosmetyk_list(r):
                """
                Determines the appropriate cosmetics list based on given cathegory.

                This function determines the appropriate list of cosmetics based on the given product category or 
                list of all cosmetics in database if cathegory is None.
                
                Parameters:
                r (str): The product category.

                Returns:
                Form: An instance of the specific form based on the provided category.
                """
                
                try:
                    k = Kosmetyk.kosmetyk_map(r).objects.all()
                except:
                    return []             
            
                return [f"{x.get_Marka()}, {x.get_Nazwa()}" for x in k]
            

            def get_kosmetyczka(cls, user: User, check: bool = False) -> Tuple[QuerySet, bool]:

                try:
                    y = user.wKosmetyczce.all()
                    print("y = ", y)
                except:
                    x = "Twoja kosmetyczka niestety jest pusta!"
                    if check:
                        return x, False
                    else:
                        return x
                else:
                    if check:
                        return y, True
                    else:
                        return y

                        
                
            class Meta:
                
                verbose_name_plural = "Kosmetyki"
                
                
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
   
class workingsKosmetyk(models.Model):
     
     """unregistered model"""
     
     kolejnosc = models.OneToOneField(Kosmetyk, on_delete=models.CASCADE)
     nazwa= models.CharField(max_length=300)

     
     def __str__(self):
         return f"kolejnosc = {self.kolejnosc}, {self.nazwa}"
     def get_kolejnosc (self):
        return self.kolejnosc
     def get_nazwa (self):
        return self.nazwa

     def set_kolejnosc(self, kosmetyk):
        self.kolejnosc = kosmetyk
     def set_nazwa (self, n):
        self.nazwa = n

     def set_work(x) :
         """
         Sets the new workingsKosmetyk based on the provided Kosmetyk item.
            
         It creates the workingsKosmetyk instance with one to one relationship with given Kosmetyk instance and saves it.
    
     
         Parameters:
             x (str): Kosmetyk object
    
    
         Returns: None
       
         """""
         q = workingsKosmetyk()
         q.set_kolejnosc(x)  
         q.set_nazwa (f"{x.Nazwa}.{x.Marka}")
         q.save()
         return q
         
         
         
         
     def check_b(name, nazwa, t=0, lenght=None):
               
         """
         
         checks which one of the words name and nazwa is earlier in the sorted list
         by checking the position in the alphabet between the the letters at t index in words "name" and "nazwa". 
         If they are the same - the function uses it's recursion to check the following letter. 
         ()
     
         Parameters:
             name (str): name of cosmetic searched for
             nazwa (str): name of cosmetic choosen to compare by bisection search
             t(int): index of letter checked
             *since the database does not allowe two cosmetics with the same name, we 
    
    
         Returns: 
             True if name[t] is earlier in alphabet(hencename is earlier than nazwa), 
             False if name[t] is later in alphabet,
             recursion if letters are the same.
         
       
         """""
         # almost the same words, but one longer
         if t == 0:
            
             a= len(name)
             b = len(nazwa)
             
             if a>b:
                 lenght = a-2
             else:
                 lenght = b-2
            
         elif lenght == 1:
             if len(name)<len(nazwa):
                 return True
             elif len(name)>len(nazwa):
                 return False
             else:
                 pass
         
            
         if name[t] < nazwa[t]:
             
             return True
         
         elif name[t] > nazwa[t] : 
             
             return False
         
         else: 
             return workingsKosmetyk.check_b(name, nazwa, t+1, lenght-1)
         
     def bisection(name, lista):
           
       """
         Bisection search for cosmetics.
         
         The function performes the bisection search on alphabrticaly ordered workingsKosmetyk based on given name.
         It uses check_b() function to establish if given name should be in lower or highrt part of list if
         both checked first letters are equal,
         
         Parameters:
         name (str): cosmetic's name
         lista (list): list of all cosmetics in workingsKosmetyk (or cosmetics yet unrejected)
         q (int): position of the letter beeing currently checked 
        
        Returns:
        Kosmetyk
        
       """
       lista_bi=lista.copy()

       q=0
       dlugosc = len(lista_bi)

       if dlugosc >2 :
           pozycja_l =  [int((dlugosc-1)/2)]
       elif dlugosc ==2:
           pozycja_l = [0,1]
       else:
           pozycja_l = [0]
  
       L = name[q]
 
       for pozycja in pozycja_l:     
           x = lista_bi[pozycja]
           nazwa = x.nazwa        
           P = nazwa[q]
    
           if name == nazwa:
               return x.kolejnosc
           
           elif P>L:
                del lista_bi[pozycja:]
               
           
           elif P<L:
                del lista_bi[:pozycja]
  
               
           else:
               if workingsKosmetyk.check_b(name, nazwa, q+1 )== True:
                    del lista_bi[pozycja:]
       
                   
               else:
                    del lista_bi[:pozycja]
           
       return workingsKosmetyk.bisection(name, lista_bi)
        
    

         
     def get_PK(name):
         
         """
         Allows to identify the position of Kosmetyk in the database.
         
         This function identifyies the position of Kosmetyk in the database 
         based on the name, and the working model "workingsKosmetyk'.
         
         Parameters:
             name (str): Cosmetic's name.
         
         Returns:
             Kosmetyk
         
         
         """
         
         
         lista = workingsKosmetyk.all() 
         kosmetyk = workingsKosmetyk.bisection(name, lista)
         
         PK = kosmetyk.id
         
         return PK
         
                
     
     class Meta:
         ordering = ['nazwa']
                

class Szampon (Kosmetyk):
    
        

    MOC_CHOICES = [
    ( "Łagodny", "Łagodny"), 
    ("Średni","Średni"), 
    ("Rypacz (mocny)", "Rypacz (mocny)"), 
    ]

    Rodzaj = models.ForeignKey(Rdz , to_field = "Rodzaj",  on_delete=models.CASCADE, related_name="Szampony", default = "Szampon")
    Moc = models.CharField ( max_length=300, choices = MOC_CHOICES)

    def get_Moc (self):
        return self.Moc
    

    def set_Moc (self, m):
        self.Moc = m
 
    
 
    class Meta:
        
        verbose_name_plural = "Szampony"
    
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
 

    Rodzaj = models.ForeignKey(Rdz, to_field = "Rodzaj", on_delete=models.CASCADE, related_name="Odżywki",  default="Odżywka")

     

        
    class Meta:
         
         verbose_name_plural = "Odżywki"
     
class Maska (O_M):
        
    Rodzaj = models.ForeignKey(Rdz, to_field = "Rodzaj", on_delete=models.CASCADE, related_name="Maski", default="Maska")


    
    class Meta:
         
         verbose_name_plural = "Maski"

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
        
        
        class Meta:
         
         verbose_name_plural = "Stylizatory"
        
        

    
class Żel (Stylizator):
    
    Rodzaj = models.ForeignKey(Rdz, to_field = "Rodzaj",  on_delete=models.CASCADE, related_name="Żele",   default="Żel")
 
        
    class Meta:
            
            verbose_name_plural = "Żele"
     
class Pianka (Stylizator):
    
    Rodzaj = models.ForeignKey(Rdz, to_field = "Rodzaj", on_delete=models.CASCADE, related_name="Pianki",  default="Pianka")

    
    class Meta:
          
          verbose_name_plural = "Pianki"
          
class Krem (Stylizator):
    
   
    Rodzaj = models.ForeignKey(Rdz, to_field = "Rodzaj",  on_delete=models.CASCADE, related_name="Kremy",  default="Krem")


  
        
    class Meta:
         
         verbose_name_plural = "Kremy"

class Olej (Kosmetyk):
    
    Rodzaj = models.ForeignKey(Rdz, to_field = "Rodzaj", on_delete=models.CASCADE, related_name="Oleje",  default="Olej")

   
        
    class Meta:
          
          verbose_name_plural = "Oleje"
     
class Olejek (Kosmetyk):
    
    Rodzaj = models.ForeignKey(Rdz, to_field = "Rodzaj", on_delete=models.CASCADE, related_name="Olejki",   default="Olejek")

  
    class Meta:
         
         verbose_name_plural = "Olejki"
     
class Wcierka (Kosmetyk):
    
    Rodzaj = models.ForeignKey(Rdz, to_field = "Rodzaj", on_delete=models.CASCADE, related_name="Wcierki",   default="Wcierka")

  
        
    class Meta:
         
         verbose_name_plural = "Wcierki"
     
class Peeling (Kosmetyk):
    
    Rodzaj = models.ForeignKey(Rdz, to_field = "Rodzaj", on_delete=models.CASCADE, related_name="Peelingi",   default="Peeling")
   

    class Meta:
         
         verbose_name_plural = "Peelingi"


        
      
            
    
        
        

   
    
  