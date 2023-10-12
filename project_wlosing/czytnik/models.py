from django.db import models

from produkty.models import Kosmetyk


def make_list(s):
    '''zrobi listę elementów z długiego stringu'''
    li = str(s)
    li = li.split(', ')
    return li


def tłumaczenie (skład):
    """bierze za argument listę składników
    tutaj będzie funkcja która będzie tłumaczyła skład"""
    PL = []
    for x in skład:
        n = Składnik.meaning(x)
        PL = PL.append(n)
    return  PL


class Składnik(models.Model):
  
      INCI = models.CharField(max_length=300)
      PL = models.CharField(max_length=300)
           
      
      
      
          
      def get_INCI(self):
        return self.INCI
      def get_PL(self):
        return self.PL
      def set_INCI(self, inci):
        self.INCI = inci
      def set_PL(self, pl):
        self.PL = pl
    
            
      def meaning (inci):
          
          
          """Bierze za argument skłanik
          do każdego składnika INCI z przypisuje wartosć PL
          zwraca pl"""
          
          try:
              n = Składnik.objects.get(INCI=inci)
          
          except:
              return "Error - brak składnika w bazie"
          
          PL = n.get_PL()
           
          
          return PL
      
class Skład (models.Model):
        
    
        Kosmetyk = models.OneToOneField(Kosmetyk, on_delete=models.CASCADE, related_name="Skład",) 
        skład_INCI = models.CharField(max_length=300, )
        skład_INCI_list = make_list(skład_INCI) 
        """do przemylenia - dodać funkcję sczytania składu ze zdjęcia"""
        skład_PL =  tłumaczenie(skład_INCI_list) 
      

        def get_skład_INCI(self):
            return self.skład_INCI
        def get_skład_PL(self):
            return self.skład_PL
        def set_skład_INCI(self, inci):
            self.skład_INCI = inci
        def set_skład_PL(self, pl):
            self.skład_PL = pl
            
