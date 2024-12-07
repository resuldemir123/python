import numpy as np


#python list
py_list=[1,2,3,4,5,6,7,8,9]

#nump array
np_array=np.array([1,2,3,4,5,6,7,8])


print(type(np_array))

np_multi=np_array.reshape(3,3) # çok boyutlu dizi haline getirdik

print(np_multi)

print(np_multi.ndim)

