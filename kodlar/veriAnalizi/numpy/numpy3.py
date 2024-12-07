import numpy as np


numbers1=np.random.randint(10,100,6)
numbers2=np.random.randint(10,100,6)

print(numbers1)
print(numbers2)

result=numbers1 + numbers2 # bunların aynı indekslerindeki sayılarını toplar ve yazar
result=numbers1 + 10 #dizideki her elemanın üzerine 10 ekler
result=np.sin(numbers1) # dizinin içindeki sayıların sinüsünü alır

mnubers1=numbers1.reshape(2,3)
mnubers2=numbers1.reshape(2,3)

print(mnubers1)
print(mnubers2)

result=np.vstack((numbers1,numbers2)) #bu dizileri birleştirir

result=numbers1 >=50 #elemanlarınn 5 ten büyük olup olamadığını gösterir


print(result)



