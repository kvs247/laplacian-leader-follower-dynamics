import datetime
import numpy as np

matrix = [
    [1, 2, 3],
    [3, 2, 1],
    [1, 3, 2]
]

print(np.linalg.eig(matrix))

start = datetime.datetime.now()
for i in range(int(3e5)):
    x = np.linalg.eig(matrix)
    y = x[0]
print(f'np.linalg.eig runtime: {datetime.datetime.now() - start}')

start = datetime.datetime.now()
for i in range(int(3e5)):
    x = np.linalg.eigvals(matrix)
print(f'np.linalg.eigvals runtime: {datetime.datetime.now() - start}')