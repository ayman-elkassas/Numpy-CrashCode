# using array-scalar type

# to determine type of each element in array

import numpy as np

dt=np.dtype(np.int32) # int32 eq string 'i4'
print (dt)

# name can be used to access content of age column
dt = np.dtype([('age',np.int8)])
a = np.array([(10,),(20,),(30,)], dtype=dt)
print(a['age'])

student=np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])
a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype=student)
print(a['age'])
print(a)