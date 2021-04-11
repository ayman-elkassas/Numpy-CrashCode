import numpy as np

a=np.arange(1,5)
b=np.arange(6)
n=np.arange(6)
c=np.zeros(10)

print(np.concatenate((a,b),out=c))
print(c)

# vertical stack
print(np.vstack((b,n)))
print(np.hstack((b,n)))

print(np.split(b,2))
# print(np.vsplit(b,2))
# print(np.hsplit(b,2))