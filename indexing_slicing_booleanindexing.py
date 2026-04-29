import numpy as np

#indexing
a1 = np.array([[1,2], [3,4]])
b1 = a1[0,1]
print(b1)

#slicing
a2 = np.array([[1,2,3,4], [5,6,7,8]])
b2 = a2[0,:]
b3 = a2[0,1:3]
b4 = a2[:,0]
b5 = a2[-1,-2]
print(b2)
print(b3)
print(b4)
print(b5)

#Boolean indexing