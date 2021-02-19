# Zadanie nr 11

import numpy as np

x = np.arange(12).reshape(1,12)

print(x)

print(x.shape)

q = x.reshape((3,4))
w = x.reshape((4,3))
e = x.reshape((2,6))

a = q.ravel()
s = w.ravel()
d = e.ravel()

print(a)
print(a.shape)

print(s)
print(s.shape)

print(d)
print(d.shape)