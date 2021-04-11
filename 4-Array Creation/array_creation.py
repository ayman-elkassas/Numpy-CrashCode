import numpy as np
x = np.empty([3,2], dtype=int)
print (x)

x=np.zeros(5,dtype=int)
print(x)

# custom type
x = np.zeros((2,3), dtype=[('x', 'i4'), ('y', 'i4')])
y=np.ones((2,3), dtype=[('x', 'i4'), ('y', 'i4')])
print(x,y)

