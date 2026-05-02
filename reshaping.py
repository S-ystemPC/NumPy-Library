import numpy as np

a = np.arange(1,7)
print(a)
print(a.shape)

# reshape
b = a.reshape((2,3))
print(b)
print(b.shape)

# reshape
c = a.reshape((3,2))
print(c)

# create new axis
d = a[np.newaxis, :]
print(d)
print(d.shape)

e = a[ :, np.newaxis]
print(e)
print(e.shape)