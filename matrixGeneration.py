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

# generate random Laplacian matrix
def generateLaplacianMatrix(dim):
    adjacencyMatrix = generateAdjacencyMatrix(dim)
    i = 0
    for row in adjacencyMatrix:
        adjacencyMatrix[i][i] = -np.sum(row)
        i += 1

    return -adjacencyMatrix

# add padding
def padding(arr, dim):
    while arr.size < dim:
        arr = np.append([0], arr)
    return arr
# print(padding(np.array([1,2,3]), 7))

# generate all Laplacians matrice for given dimension
def getAllLaplacianMatrices(dim):
    result = np.array([])
    numElementsAboveDiag = (dim / 2) * (dim - 1) # explain
    numMatricesTotal = int(2 ** numElementsAboveDiag - 2)
    allBinaryVectors = matrixMath.getBinaryVectors(dim)
    for elements in allBinaryVectors:
        tempMatrix = np.array([])
        for rowNumber in range(1, dim + 1):
            row = elements[0:dim - rowNumber]
            elements = elements[dim - rowNumber:]
            row = padding(row, dim)
            tempMatrix = np.append(tempMatrix, row)
        result = np.append(result, tempMatrix).astype(int)
    result = np.reshape(result, (numMatricesTotal, dim, dim))
    return result

x = getAllLaplacianMatrices(3)
print(x)
