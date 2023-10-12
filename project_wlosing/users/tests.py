from django.test import TestCase

# Create your tests here.


def check_password(password):
    le = len(password)
    
    try: 
        le >= 8
        
    except: 
        return False
    
    if password.islower() == True :
        return False
        
           
    for p in password:
        W = True
        try: 
            int(p)
            
            break
            
        except:
            W = False
        
        
    if W == True:
            return True
    else:       
        return False
        
    
def check_email(mail):
    
    try:
        
        a = mail.index("@")
        
        b = mail.rindex(".")
        c = len(mail)-b-1
        print("war 1 - ok")
        
        
    except:
        return False
    
    
    print(b , c)
          
    if c>= 2 and c<=3:
       print("war2 - ok")
       pass
              
    else:
        return False
    
    if a<b:
        print("wa3 - ok")
        pass
    else:
        return False
    
    return True

em = {"ola" : "Nieprawidłowy", 
      "ola@": "Nieprawidłowy", 
      "ola@." : "Nieprawidłowy",
      "ola.com" : "Nieprawidłowy", 
      "ola.mail@com": "Nieprawidłowy", 
      "ola.mail@pl" : "Nieprawidłowy",
      "ola@mail.c" : "Nieprawidłowy", 
      "ola@mail.com": "Prawidłowy", 
      
      }
pas = {"example":"Nieprawidłowy",
       "example8":"Nieprawidłowy",
       "Exa8":"Nieprawidłowy",
       "exr9mple":"Nieprawidłowy",
       "exampleE":"Nieprawidłowy",
       "examp8leE":"Prawidłowy",
            
       }

for e in em.keys():
    
    x = check_email(e)
    
    print(f'email {e} ma prawidłowy format- {x}')
    
    
for p in pas.keys():
    x = check_password(p)
    
    print(f'hasło {p} ma prawidłowy format- {x}')