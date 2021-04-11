# N-Dimensional array
import numpy as np

# 1 dim
a=np.array([1,2,3])
print(a)

# 2 dim
a = np.array([[1, 2], [3, 4]])
print(a)

# minimum dimensions
a=np.array([1, 2, 3,4,5], ndmin=2)
print(a)

# minimum dimensions
a=np.array([1, 2, 3,4,5],dtype=complex)
print(a)
