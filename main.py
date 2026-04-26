# day 1
import numpy as np
# print(np.__version__)

a = np.array([2,4,5])
print(a)
print(a.shape)
print(a.dtype)
print(a.ndim)
print(a.size)
print(a.itemsize)

# day 2
print(a[0])
a[0] = 10
print(a)

b = a * np.array([4,0,1])
print(b)