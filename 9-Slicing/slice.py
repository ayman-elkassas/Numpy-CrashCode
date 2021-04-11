import numpy as np

a=np.array([[1,2,3,10,1],[4,5,6,7,3]])
# print(a)
# [start:end:step]
# note end must be end+1

# get intersection sub array from overall
print(a[1:3:,0:2:])


