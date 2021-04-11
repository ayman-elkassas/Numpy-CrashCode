import numpy as np

# convert list to ndarray
x = [1,2,3]

# convert tuple to ndarray
y = (1,55,88)

a = np.asarray((x),dtype=int)
a = np.asarray((y),dtype=int)

print (a)

# a[0,0]=5
# print(a)

# ndarray from list of tuples
x = [(1,2,3),(4,5)]
a = np.asarray(x)
print (a)

s = b'Hello World'
t = np.frombuffer(s,dtype="|S1")
print (t)

# obtain iterator object from list
list = range(5)
it = iter(list)
print(it)
# use iterator to create ndarray
x = np.fromiter(it, dtype=float)
print(x)

x = np.arange(5, dtype=float)
print (x)

# if you want to make array determine start, end and number of elements inside this array
arrayList=np.linspace(1,100,num=4)
print(arrayList)