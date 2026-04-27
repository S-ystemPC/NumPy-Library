import numpy as np

a1 = np.array([1,2,3])
a2 = np.array([4,5,6])

dot = np.dot(a1,a2)
print(dot)

dot = a1 @ a2
print(dot)