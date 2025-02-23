def not_hesapla(satir):
    satir=satir[:-1]
    liste=satir.split(':')
    
    ogrenciAdi=liste[0]
    notlar=liste[1].split(',')
    
    not1=int(notlar[0])
    not2=int(notlar[1])
    not3=int(notlar[2])
    
    ortalama=(not1+not2+not3)/3

    if ortalama>=30 and ortalama<=40:
        harf="AA"
    elif ortalama>=25 and ortalama<=29:
            harf="BA"
    elif ortalama>=20 and ortalama<=24:
            harf="BB"
    elif ortalama>=15 and ortalama<=20 :
        harf="CB"   
    else:
        harf="FF"
        
    return ogrenciAdi+':'+harf+"\n"                
def ortalamalari_oku():
    with open("sinav_notlari.txt", "r", encoding="utf-8") as file:
        for satir in file:
           print(not_hesapla(satir))

def not_gir():
    ad = input('Öğrenci adı :')
    soyad = input('Öğrenci soyadı :')
    not1= input(' not1 :')
    not2= input(' not2 :')
    not3= input(' not3 :')
    
    with open("sinav_notlari.txt", "a" , encoding="utf-8") as file:
     file.write(ad+' '+ soyad+':'+not1+','+not2+','+not3+'\n')  

def notlari_kayitet():
     with open('sinav_notlari.txt','r',encoding='utf-8') as file:
         liste=[]
         for i in file:
             liste.append(not_hesapla(i))
             
         with open('sonuclar.txt','w',encoding='utf-8') as file2:
             for i in liste:
                 file2.write(i)
                     


while  True:
    islem=input('1-Notları Oku\n2- Not Gir\n3- Notları Kayıt et\n4-Çıkış ')
    
    if islem=='1':
        ortalamalari_oku()   
    elif islem=='2':
        not_gir()
    elif islem=='3':
        notlari_kayitet()
    else:
        break