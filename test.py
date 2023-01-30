import numpy as np

arr = np.array([1,2,3,4])

def foo(x):
    if (x > 2):
        return x - 1
    else:
        return x

arr = foo(arr)

print(arr)