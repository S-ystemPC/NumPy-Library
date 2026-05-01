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

# Boolean indexing
a3 = np.array([[1,2], [3,4], [5,6]])
print(a3)
bool_index = a3 > 2
print(bool_index)
print(a3[bool_index])
# Or
print(a3[a3 > 2])

# where 
b6 = np.where(a3 > 2, a3, -1)
print(b6)

# fancy indexing
a4 = np.array([10,19,30,41,50,61])
b7 = [1,3,5]
print(a4[b7])
# Use case of fancy indexing
even = np.argwhere(a4 % 2 == 0).flatten()
print(a4[even])