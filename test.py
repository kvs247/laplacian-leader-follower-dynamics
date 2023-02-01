import numpy as np

a = np.array([1, 2, 0, 0])

print(len(np.where(a == 0)[0]))

print(np.delete(a, 0))