import numpy as np

myArr = np.array([[1,2,3],[4,5,6],[7,8,9]])

x = myArr.flatten().astype(str)
print(''.join(x))
