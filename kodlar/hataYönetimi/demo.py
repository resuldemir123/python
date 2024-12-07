liste=["1","2","5a","10b","abc","10","50"]

#1:cListe elemanları içindeki sayısal değerleri bulunuz
#for x in liste:
#    try:
#        result=int(x)
#        print(result)
#    except ValueError:
#        continue

# 2: Kullanıcı 'q' değerini girmedikçe aldığınız her inputun sayı
#olduğundan emin olunuz aksi takdirde hata mesajı yazın.
#while True:
#    sayi=input('sayi: ')
#    if sayi=='q':
#            break
         
#    try:
#            result=float(sayi)
#            print("girdiğiniz sayi: ",result)
#    except ValueError:
#            print("geçersiz sayı")
#            continue

# 3: Girilen parola içinde türkçe karakter hatası verir
#turkce_karakter=["r","e","a","i","s","c","u"]
#parola=input('parola:')

#for i in parola:
#    if i in turkce_karakter:
#        raise TypeError('Parola türkçe karakter içeremez')
#    else:
#        pass

#4: Faktöriyel fonksiyonu oluşturulup fonksiyona gelen değer için hata mesajı verin

def faktoriyel(x):
    x=int(x)
    
    if x<0:
        raise ValueError('Negatif deger')
    
    result=1
    
    for i in range(1,x+1):
        result *=i
        
        
    return    result

faktoriyel(-1)