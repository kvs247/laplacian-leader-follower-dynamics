import numpy as np

def printMatrix(matrix):
    n = np.shape(matrix)[0]
    print('')
    for i in range(n):
        row = '|'
        for j in range(n):
            value = int(matrix[i][j])
            if value < 0:
                row += f' {value}' # one space
            else:
                row += f'  {value}' # two spaces
        row += ' |'
        print(row)
    print('')

# returns true if any pair of values within the array are within 1e-10 of each other
def hasRepeatedValue(eigenValues):
    dim = np.shape(eigenValues)[0]
    for i in range(dim):
        for j in range(i+1, dim):
            if abs(eigenValues[i] - eigenValues[j]) < 1e-10:
                return True
    return False

# get 2D array containing all binary vectors for the given dimension as an array
# note: this does not include the zero vector or all 1s vector
def getBinaryVectors(dim):
    result = []
    for i in range(1, (2 ** dim) - 1):
        binaryString = bin(i)[2:].rjust(dim, '0')
        binaryVector = np.array(list(binaryString)).astype(int)
        result.append(binaryVector)
    return np.array(result)

# get array whose first value is array of eigenvalues and second value is array of eigenvectors, using the same index
def getEigenState(matrix):
    eigenState = np.linalg.eig(matrix)
    eigenValues = eigenState[0].real
    eigenVectors = np.transpose(eigenState[1]).real 
    eigenValues[abs(eigenValues) < 1e-10] = 0 # zero float correction 
    eigenVectors[abs(eigenVectors) < 1e-10] = 0 # zero float correction
    return [eigenValues, eigenVectors] 

# determine controllability class of given matrix
def pbhTest(matrix, eigenValues, eigenVectors):

    if len(np.where(eigenValues == 0)[0]) > 1:
        return 'completely uncontrollable (disconnected)'

    if hasRepeatedValue(eigenValues):
        return 'completely uncontrollable (degenerate)'

    dim = np.shape(matrix)[0]
    uncontrollablePairs = 0
    controllablePairs = 0

    goToNext = False
    for i in range(1, (2 ** dim) - 1):
        binaryString = bin(i)[2:].rjust(dim, '0')
        controlVector = np.array(list(binaryString)).astype(int)

        nonZeroPairs = 0
        for eigenVector in eigenVectors:
            if goToNext:
                goToNext = False
            innerProduct = np.dot(controlVector, eigenVector)
            if (abs(innerProduct) < 1e-10):
                uncontrollablePairs += 1
                goToNext = True
                break
            else:
                nonZeroPairs += 1
        if nonZeroPairs == dim:
            controllablePairs += 1
            
        if (uncontrollablePairs > 0 and controllablePairs > 0):
            return 'conditionally controllable'

    if uncontrollablePairs == (2 ** dim) - 2:
        return 'completely uncontrollable (nondegenerate)'
    elif uncontrollablePairs == 0:
        return 'essentially controllable'
    else:
        print('error, no controllability class found')












