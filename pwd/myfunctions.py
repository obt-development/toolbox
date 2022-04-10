import string
import random
from datetime import timedelta, date

   

def choice_component(six_month, twelves_month, res_num, res_char, res_spec, nb ):
    
    """
    Password generator with configurable validity period.

    Args:
        six_month (Boolean): Duration calculated for six months.
        twelves_month (Boolean): Duration calculated for twelve months.
        res_num (Boolean): adding numeric values.
        res_char (Boolean): add upper and lower case letters.
        res_spec (Boolean): add special characters.
        nb (Integer): number of password characters.
    """
    
    # Attrinution des variables
    num = string.digits
    char = string.ascii_letters
    spec = '!@#$%^&*-_'
    error = False
    check = False

    
    # réglage de la date de validité
    current_date = date.today()
    if six_month and twelves_month==0:
        limit_date = current_date + timedelta(days=182.5)
    elif twelves_month and six_month==0:
        limit_date = current_date + timedelta(days=365)
    elif twelves_month and six_month:
        limit_date = "vous devez ne choisir qu'une durée"
        error = True
    elif six_month==0 and twelves_month==0:
        limit_date = "illimité"
        # error = True
        
    
    # Création du mot de passe
    if not error :
        # Si tout est choisi
        if res_num ==1 and res_char==1 and res_spec==1 : 
            word= num + char + spec
            pwd =''.join(random.choices(word, k=nb))
            while check == False : 
                check =  (any(item in num for item in pwd) and any(item in spec for item in pwd) and any(item in char for item in pwd))
                pwd =''.join(random.choices(word, k=nb))

        # Si les caractères spéciaux sont exclus
        elif  res_num ==1 and res_char==1 and res_spec==0 :
            word= num + char
            pwd =''.join(random.choices(word, k=nb))
            while check == True : 
                check =  (any(item in num for item in pwd) and any(item in char for item in pwd))
                pwd =''.join(random.choices(word, k=nb))

        # Si les lettres sont exclus
        elif  res_num ==1 and res_char==0 and res_spec==1 :
            word= num + spec
            pwd =''.join(random.choices(word, k=nb))
            while check == True : 
                check =  (any(item in num for item in pwd) and any(item in spec for item in pwd))
                pwd =''.join(random.choices(word, k=nb))

        # Si les chiffres sont exclus
        elif  res_num ==1 and res_char==0 and res_spec==1 :
            word= char + spec
            pwd =''.join(random.choices(word, k=nb))
            while check == True : 
                check =  (any(item in spec for item in pwd) and any(item in char for item in pwd))
                pwd =''.join(random.choices(word, k=nb))
                
        # Si les caractères spéciaux et les lettres sont exclus
        elif res_num ==1 and res_char==0 and res_spec==0 : 
            word= str(num)
            pwd =''.join(random.choices(word, k=nb))
            
        # Si les caractères spéciaux et les chiffres sont exclus
        elif res_num ==0 and res_char==1 and res_spec==0 : 
            word= char
            pwd =''.join(random.choices(word, k=nb))
        
        # Si les chiffres et les lettres sont exclus    
        elif res_num ==0 and res_char==0 and res_spec==1 : 
            word= spec
            pwd =''.join(random.choices(word, k=nb))
        
        print(f"Le mot de passe est : {pwd}  et la date de validité est : {str(limit_date)}.")
    else:
        print(limit_date)
     
choice_component(1, 0, 1, 1, 1, 8)