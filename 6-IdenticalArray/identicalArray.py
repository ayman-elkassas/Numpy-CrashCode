import numpy as np

# empty is random array
# identicalArray=np.empty(5)
# identicalArray=np.ndarray(5,dtype=int)

# identical array
identicalArray=np.eye(5)

# k is parameter determine ones 
identicalArray=np.eye(5,k=-1)

print(identicalArray)