import numpy as np
a1 = np.array([[1,2], [3,4]])

print(a1)
print(a1.shape)


a2 = np.array([[1,2,6], [3,4,8]])
print(a2)
print(a2.shape)

print(a2[0])
print(a2[0][0])


a3 = np.array([[1,2,6], [3,4,8]])
# To print all rows an 0'th column
print(a3[:,0])

# To print 0'th row and all columns
print(a3[0,:])

# Transpose
a4 = np.array([[1,2,3], [4,5,6]])
print(a4.T)

# Inverse
a5 = np.array([[1,2], [3,4]])
print(np.linalg.inv(a5))

# Determinant
a6 = np.array([[1,2], [3,4]])
print(np.linalg.det(a6))

# diagonal element
a7 = np.array([[1,2], [3,4]])
print(np.diag(a7))

# printing diagonal matrix
a8 = np.array([[1,2], [3,4]])
c = np.diag(a8)
print(np.diag(c))