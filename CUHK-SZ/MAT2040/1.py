import numpy as np
from ula_numpy import *

# Create a 2*4 matrix
A = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(2, 4)
print(A)

A = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(A)

#RREF of a matrix
A = np.array([
    [-1, -2, 2, -1],
    [2, 4, -1, 5],
    [1, 2, 0, 3]],
    dtype = float)
print(A)
print(rref(A))
