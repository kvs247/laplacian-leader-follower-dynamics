import matrixMath
import numpy as np

# for i, j indexing a matrices rows and columns, returns 0 for elements on or below diagonal and either 1 or 0 at random for elements above the diagonal
def generateRandomElement(i, j):
    if (j <= i):
        return 0
    else:
        return np.random.choice([0,1])