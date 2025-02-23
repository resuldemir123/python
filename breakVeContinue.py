i=0

while (i < 10):
    if i==5:
        break  #Şart sağlandığında döngüden çıkar
    print("i:",i)
    i+=1
print("\n")

a=0
while (a < 10):
    if a==5 or a == 7:
        a += 1
        continue
    print("a:",a)
    a +=1
