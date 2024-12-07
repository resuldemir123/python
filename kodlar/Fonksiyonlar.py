def selamla(): #def fonksiyon tanımlar
    print("merhaba")
    print("nasılısn")

selamla()


def selam(isim = "isimsiz"):
    print("merhaba",isim)

selam("resul")
selam()

def toplama(a,b,c):
    print("toplam:",a+b+c)

d = toplama(2,3,4) #fonksiyon çıktısını bir değere atamamız için return kullanmalıyız yoksa none çıkar
print(d)

def toplama(a,b,c):
    return a+b+c

toplam=toplama(2,5,7)
print(toplam)

