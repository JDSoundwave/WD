# Zadanie nr 2

import numpy as np

x = np.array([[2, 4, 7], [13, 4, 9], [5, 17, 6]])

y = np.array([[1, 2, 3, 7], [9, 2, 4, 8], [3, 15, 4, 1], [9, 9, 7, 4]])

print(x.min(axis = 1))

print(x.min(axis = 0))

print(y.min(axis = 1))

print(y.min(axis = 0))