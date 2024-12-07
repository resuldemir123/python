import datetime
import os  #işletim sistemi ile ilgili bilgiler sunar

result=dir(os)
result=os.name #işletim sis. çeşidini söyler
result=os.getcwd()#dosyanın konumunu söyler

#os.chdir("C:\\") 
#os.mkdir("newDirectory") yeni klasör oluştururlar
os.rename("newDirectory","yeniKlasor")
#os.listdir("C:\\") C klasörünü listeler
#os.removedirs("yeniKlasor") o klasörü siler

#for dosya in os.listdir("C:\\"):
#    if dosya.endswith('.py'):
#        print(dosya)


#result=os.stat("datetime.py") #bu klasör hakkında bilgi verir
#result=datetime.datetime.fromtimestamp(result.st_ctime) #oluşturulma tarihi
#result=datetime.datetime.fromtimestamp(result.st_atime) #son erişilme tarihi
#result=datetime.datetime.fromtimestamp(result.st_mtime) #değiştirilme tarihi

#os.system("notepad.exe") systemde bulur ve açar

#path :bir dosyanın uzantısının nasıl değiştirilir

result=os.path.abspath("os.py")
result=os.path.dirname(os.path.abspath("os.py")) # dizin ismini alıyoruz
result=os.path.exists("os.py") #sorgular boolean döndürür
result=os.path.isdir( "C:/python/kodlar>")
result=os.path.join("C:\\","deneme")
result=os.path.split("C:\\deneme")

print(result)