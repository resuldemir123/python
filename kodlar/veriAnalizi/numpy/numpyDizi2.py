import numpy as np

numbers=np.array([1,2,3,5,6,7,8,8,8])

result=numbers[5]
result=numbers[0:3]


numbers2=np.array([[1,2,3,5],[6,7,8],[8,8,9]])
result=numbers2[2]
result=numbers2[2,1]
result=numbers2[:,2] #2. kolondaki tüm değerler gelir
result=numbers2[:,0:2] #kolonlardaki 0 -2.arasındaki tüm değerleri getirir



