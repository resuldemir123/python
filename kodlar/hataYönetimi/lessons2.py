#hata nesnesi oluşturma

#x=int(input('x:'))

#if x>5:
#    raise Exception('x 5 den büyük deger alamaz')


def check_password(psw):
    import re
    if len(psw)<8:
        raise Exception("parola en az 8 karakter olmalı")
    elif not re.search("[a-z]",psw):
        raise Exception("parola küçük harf içermelidir")
    elif not re.search("[A-Z]",psw):
            raise Exception("parola büyük harf içermelidir")
    elif not re.search("[0-9]",psw):
            raise Exception("parola rakam içermelidir")
    elif not re.search("[_@$]",psw):
        raise Exception("parola alpha numeric karakter içermelidir")
    elif re.search("\s",psw):
        raise Exception("parola boşluk içermemelidir")
    else:
        print("geçerli parola")
    
password="a12345678C_"

try:
    check_password(password)
except Exception   as ex:
    print(ex)      
else:
    print("geçerli parola: else")    
    
finally:
    print("validation tamamlandı")   
    
    
     