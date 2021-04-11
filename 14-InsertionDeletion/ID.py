import numpy as np

arr=np.array([[1,2],[3,4]])

print(np.insert(arr,1,23))
print(np.insert(arr,1,23,axis=0))
print(np.insert(arr,1,[1,5],axis=1))

print(np.append(arr,[[5,0]],axis=0))

print(np.delete(arr,2))
