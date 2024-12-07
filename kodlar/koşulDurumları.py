yas=int(input("yasşınızı giriniz:"))

if yas > 18:
    print("mekana girebilirsiniz...")
else:
    print("mekana giremezsiniz")


harf=input("Harfi giriniz:")

if harf == "B":
    print("Beşiktaşlısınız")
elif harf == "G":
   print("Galatsaraylısınız")
elif harf == "F":
   print("Fenerbahçelisiniz")
elif harf == "A":
    print("Anadolu takımlarını destekliyorsunuz")
else:
    print("Hatalı bir seçenek giridniz")

