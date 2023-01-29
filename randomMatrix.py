import matrixMath
import numpy as np

# for i, j indexing a matrices rows and columns, returns 0 for elements on or below diagonal and either 1 or 0 at random for elements above the diagonal
def generateRandomElement(i, j):
    if (j <= i):
        return 0
    else:
        return np.random.choice([0,1])

# generate random Adjacency matrix
def generateAdjacencyMatrix(dim):
    if (dim < 3):
        raise Exception('need at least dim = 3 for matrix generation')

    result = np.array([])
    for i in range(dim):
        for j in range(dim):
            result = np.append(result, generateRandomElement(i, j))
    
    result = np.reshape(result, (dim, dim))
    resultTranspose = np.transpose(result)
    result = result + resultTranspose

    return result