
    
    
#with open("new file.txt","r+",encoding="utf-8") as file:
#    file.seek(55)
#    file.write("deneme ") 
    
#with open("new file.txt","r+",encoding="utf-8") as file:
#    print(file.read())    

#!!Sayfa sonuna güncelleme

#with open("new file.txt","a",encoding="utf-8") as file:
#    file.write("\nRONDON")



#!!Sayfa başına güncelleme
    
#with open("new file.txt","r+",encoding="utf-8") as file:
#    print(file.read())
#    conten=file.read()
#    conten="rasmus rasul\n"  + conten
#    print(conten)
    
    
#with open("new file.txt","r",encoding="utf-8") as file:
#    print(file.read())    

#!!Satfa ortasında güncelleme
with open("new file.txt","r+",encoding="utf-8") as file:
    list=file.readlines()
    list.insert(1,"bedirhan\n")
    file.seek(0)
    for i in list:
        file.write(i)

with open("new file.txt","r",encoding="utf-8") as file:
    print(file.read())   