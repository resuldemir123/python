import numpy as np


#result=numpy.array([1,2,3,4,6])

#result=np.arange(1,10)

#result=np.arrange(10,100,3)

#result=np.zeros(10) 10 tane sıfır verir

#result=np.linspace(0,100,5) 0-100 arasını 5 parçaya böler

#result=np.random.randint(0,10) rastgele sayı verir

np_array=np.arange(50)
np_multi=np_array.reshape(5,10) #bize 5'e 10 luk bir dizi verir
print(np_multi.sum(axis=1)) #bize satırların toplamını verir)


#print(result)