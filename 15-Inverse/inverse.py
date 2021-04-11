import numpy as np

arr=np.array([[1,2],[3,4]])

inverseArr=np.linalg.inv(arr)

# A*A(inv)=indentity matrix

print(np.dot(arr,inverseArr))

print(np.linalg.matrix_power(arr,0))