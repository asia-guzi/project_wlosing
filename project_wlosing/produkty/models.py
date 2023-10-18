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
             
                
            def kosmetyk_list(r=None):
                """
                Determines the appropriate cosmetics list based on given cathegory.

                This function determines the appropriate list of cosmetics based on the given product category or 
                list of all cosmetics in database if cathegory is None.
                
                Parameters:
                r (str): The product category.

                Returns:
                Form: An instance of the specific form based on the provided category.
                """
                if r != None:
                    try:
                        mapping = {
                            "Szampon": Szampon.objects.all(),
                            "Odżywka": Odżywka.objects.all(),
                            "Maska": Maska.objects.all(),
                            "Wcierka": Wcierka.objects.all(),
                            "Pianka": Pianka.objects.all(),
                            "Żel": Żel.objects.all(),
                            "Krem": Krem.objects.all(),
                            "Peeling": Peeling.objects.all(),
                            "Olej": Olej.objects.all(),
                            "Olejek": Olejek.objects.all(),
                        }
                        
                        k = mapping[r]
                    except:
                        return []
                else:
                    k = Kosmetyk.objects.all()
                    
                    
                L=[]
                for x in k:
                                
                    m = x.get_Marka()
                    n = x.get_Nazwa()
                    L.append(f"{m}, {n}")
                return L
            



                
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
     
     kolejnosc = models.OneToOneField(Kosmetyk, on_delete=models.CASCADE)#, Primary_key=True)
     nazwa= models.CharField(max_length=300)
     
     def __str__(self):
         return f"pk = {self.pk}. kolejnosc = {self.kolejnosc}, {self.nazwa} "
     
     def set_work(x) :
         """
         Sets the new workingsKosmetyk based on the provided Kosmetyk item.
            
         It creates the workingsKosmetyk instance with one to one relationship with given Kosmetyk instance and saves it.
    
     
         Parameters:
             x (str): Kosmetyk object
    
    
         Returns: None
       
         """""
         x = Kosmetyk.objects.get(Nazwa=x.Nazwa)
         q = workingsKosmetyk()
         q.nazwa = x.Nazwa
         q.kolejnosc = x
         q.save()
         
         
         
         
         
     def check_b(name, nazwa, t):
               
         """
         
         checks the position in the alphabet between the the letters at t index in words "name" and "nazwa". 
         If they are the same - the function uses it's recursion to check the following letter. 
         
     
         Parameters:
             name (str): name of cosmetic searched for
             nazwa (str): name of cosmetic choosen to compare by bisection search
             t(int): index of letter checked
    
    
         Returns: 
             True if name[t] is earlier in alphabet, False if name[t] is later in alphabet,
             recursion if letters are the same.
         
       
         """""
         
         if name[t] < nazwa[t]:
             return True
         
         elif name[t] < nazwa[t] : 
             return False
         
         else: 
             return workingsKosmetyk.check_b(name, nazwa, t+1)
         
     def bisection(name, lista, q):
           
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
         
         dlugosc = len(lista)
         pozycja =  int(dlugosc/2) -1
         I = name[q]
         nazwa = ""
         
         
         while name != nazwa:
             
             x = lista[pozycja]
             nazwa = x.nazwa        
             P = nazwa[q]
             
             if P>I:
                 pozycja = pozycja-int(pozycja/2)
             elif P<I:
                 pozycja = pozycja+int(pozycja/2)
             else:
                 if workingsKosmetyk.check_b(name, nazwa, q+1 )== True:
                     pozycja = pozycja-int(pozycja/2)
                 
                 else:
                     pozycja = pozycja+int(pozycja/2)
                     
                     
         return x
         
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
         PK = workingsKosmetyk.bisection(name, lista, q=0)
         return PK
         
                
     
     class Meta:
         ordering = ['nazwa']
                

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
 

    Rodzaj = models.ForeignKey(Rdz, to_field = "Rdz", on_delete=models.CASCADE, related_name="Odżywki",  default="Odżywka")

     

        
    class Meta:
         
         verbose_name_plural = "Odżywki"
     
class Maska (O_M):
        
    Rodzaj = models.ForeignKey(Rdz, to_field = "Rdz", on_delete=models.CASCADE, related_name="Maski", default="Maska")


    
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
    
    Rodzaj = models.ForeignKey(Rdz, to_field = "Rdz",  on_delete=models.CASCADE, related_name="Żele",   default="Żel")
 
        
    class Meta:
            
            verbose_name_plural = "Żele"
     
class Pianka (Stylizator):
    
    Rodzaj = models.ForeignKey(Rdz, to_field = "Rdz", on_delete=models.CASCADE, related_name="Pianki",  default="Pianka")

    
    class Meta:
          
          verbose_name_plural = "Pianki"
          
class Krem (Stylizator):
    
   
    Rodzaj = models.ForeignKey(Rdz, to_field = "Rdz",  on_delete=models.CASCADE, related_name="Kremy",  default="Krem")


  
        
    class Meta:
         
         verbose_name_plural = "Kremy"

class Olej (Kosmetyk):
    
    Rodzaj = models.ForeignKey(Rdz, to_field = "Rdz", on_delete=models.CASCADE, related_name="Oleje",  default="Olej")

   
        
    class Meta:
          
          verbose_name_plural = "Oleje"
     
class Olejek (Kosmetyk):
    
    Rodzaj = models.ForeignKey(Rdz, to_field = "Rdz", on_delete=models.CASCADE, related_name="Olejki",   default="Olejek")

  
    class Meta:
         
         verbose_name_plural = "Olejki"
     
class Wcierka (Kosmetyk):
    
    Rodzaj = models.ForeignKey(Rdz, to_field = "Rdz", on_delete=models.CASCADE, related_name="Wcierki",   default="Wcierka")

  
        
    class Meta:
         
         verbose_name_plural = "Wcierki"
     
class Peeling (Kosmetyk):
    
    Rodzaj = models.ForeignKey(Rdz, to_field = "Rdz", on_delete=models.CASCADE, related_name="Peelingi",   default="Peeling")
   

    class Meta:
         
         verbose_name_plural = "Peelingi"


        
      
            
    
        
        

   
    
  