#try:
#    file=open("new file.txt","r")
#    print(file)
#except FileNotFoundError:
#    print("dosya okuma hatası")    
#finally:
#    print("dosya kapandı.")
#    file.close()


file = open("new file.txt","r",encoding="utf-8")

#!!for döngüsü

#for i in file:
#    print(i,end="")


#!!read() fonksiyonu

#content1=file.read()

#print("içerik 1")
#print(content1)

#content2=file.read()

#print("içerik 2")
#print(content2)


#content=file.read(5)
#content=file.read(3) en son okuma işlemi nerde kaldıysa ordan devam eder

#print(content)



#!! readline() fonksiyonu

#content=file.readline()
#content=file.readline()
#print(content)

#!! readlines() fonksiyonu

liste=file.readlines()
print(liste)

file.close()