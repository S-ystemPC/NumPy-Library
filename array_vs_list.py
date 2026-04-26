import numpy as np

l = [1,2,3]
a = np.array([1,2,3])



# append 
l.append(4)
print(l)
# Below line shoes error coz "append" is not an attribute of numpy.ndarray
# a.append(4)
# print(a)


# appending with different method
l = l + [4]
print(l)
a = a + np.array([4])
print(a)


# multiplication
l1 = [1,2,3]
a1 = np.array([1,2,3])

l1 = l1 * 2
print(l1)
a1 = a1 * 2
print(a1)


# squareroot
a2 = np.array([1,2,3])
a2 = np.sqrt(a2)
print(a2)


# log
a3 = np.array([1,2,3])
a3 = np.log(a3)
print(a3)