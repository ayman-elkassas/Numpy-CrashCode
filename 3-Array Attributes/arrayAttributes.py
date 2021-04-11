import numpy as np

a=np.array([[1,2,3],[4,5,6]])
# array is 2*3
print(a.shape)

a=np.array([[1,2,3],[4,5,6]])
# a.shape=(3,2) #OR
b=a.reshape(3,2)
print (b)

a = np.arange(24)
print (a)

a = np.arange(24)
# now reshape it
b = a.reshape(2,4,3)
print (b,b.ndim)
# b is having three dimensions

# dtype of array is now float32 (4 bytes)
x = np.array([1,2,3,4,5], dtype=np.float32)
print (x.itemsize)