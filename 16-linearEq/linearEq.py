# how to solve two linear eqs
import numpy as np

# 6x+2y-5z=13
# 3x+3y-2z=13
# 7x+5y-3x=26

x=np.array([[6,2,-5],[3,3,-2],[7,5,-3]])
y=np.array([13,13,26])

result=np.linalg.solve(x,y)
print(result)