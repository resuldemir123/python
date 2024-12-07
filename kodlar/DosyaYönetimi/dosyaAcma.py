#Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır
#Kullanımı: open(dosya_adi,dosya_erişme_modu)
#dosya erişme modu => dosyayı hangi amaçla açtığımızı belirler

#DOSYA ERİŞME MODLARI 
# "w": (write) yazma modu.Dosyayı konumda oluşturur

#file=open("new file.txt","w")
#file.close()

#file=open("new file.txt","w",encoding='utf-8')
#file.write("Resul Demir")
#file.close()

# "a": (append) ekleme.Dosya konumda yoksa oluşturulur

#file=open("new file.txt","a",encoding='utf-8')
#file.write(" Resul Demir")
#file.write("\nRasmus")
#file.close()

# "x": (create9 oluşturma.Dosya zaten varsa hata verir

file=open("new file2.txt","x",encoding='utf-8')

# "r": (read) okuma.dosya konumda yoksa haata verir

