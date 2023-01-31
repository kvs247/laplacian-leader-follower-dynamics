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
    numElementsAboveDiag = int((dim / 2) * (dim - 1)) # explain
    numMatricesTotal = int((2 ** numElementsAboveDiag) - 2)
    allBinaryVectors = matrixMath.getBinaryVectors(numElementsAboveDiag)

    k = 1
    total = np.shape(allBinaryVectors)[0]
    for elements in allBinaryVectors:
        print(f' generating matrices: {(int(k/total * 10000))/100}', end='\r')
        tempMatrixFlat = np.array([])
        for rowNumber in range(1, dim + 1):
            row = elements[0:dim - rowNumber]
            elements = elements[dim - rowNumber:]
            row = padding(row, dim)
            tempMatrixFlat = np.append(tempMatrixFlat, row)
        tempMatrix = np.reshape(tempMatrixFlat, (dim, dim))
        tempMatrixTranspose = np.transpose(tempMatrix)
        tempMatrix = tempMatrix + tempMatrixTranspose
        for i in range(dim):
            rowSum = np.sum(tempMatrix[i])
            tempMatrix[i][i] -= rowSum
        tempMatrixFlat = -tempMatrix.flatten()
        result = np.append(result, tempMatrixFlat).astype(int)
        
        k += 1
    print('')
    result = np.reshape(result, (numMatricesTotal, dim, dim))
    return result

# print(getAllLaplacianMatrices(3))

def getLaplacianFromId(id):
    dim = int(id[0:2])
    generator = int(id[2:])
    numElementsAboveDiag = int((dim / 2) * (dim - 1)) # explain
    elements = bin(generator)[2:].rjust(numElementsAboveDiag, '0')
    elements = np.array(list(elements)).astype(int)

    tempArray = np.array([])
    for rowNumber in range(1, dim+1):
        row = elements[0:dim - rowNumber]
        row = padding(row, dim)
        tempArray = np.append(tempArray, row)
        elements = elements[dim - rowNumber:]
    tempArray = np.reshape(tempArray, (dim, dim))
    tempArrayTranspose = np.transpose(tempArray)

    result = -(tempArray + tempArrayTranspose)

    for i in range(0, dim):
        result[i][i] = -np.sum(result[i])

    return result


    




