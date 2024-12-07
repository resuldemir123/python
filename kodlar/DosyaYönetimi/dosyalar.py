file = open("dosya.txt","a")#a değişiklikleri düzenliyor

file.write("bu dosya çıktısı buraya ait")
file.close()

file = open("dosya.txt","r")#r dosya içeriğini okur
veri = file.read()
print(veri)

file = open("dosya.txt","r")#r dosya içeriğini okur
file.seek(10) #seek 10 adım ileri atar
veri = file.read(10)
print(veri)

for satir in file:
    print(satir)



