import numpy as np

# determine controllability class of given matrix
def pbhTest(matrix, eigenValues, eigenVectors):
    n = np.shape(matrix)[0]
    controlSet = getControlSet(n)
    zeroCount = 0

# get array whose first value is array of eigenvalues and second value is array of eigenvectors, using the same index
def getEigenState(matrix):
    eigenState = np.linalg.eig(matrix)
    eigenValues = eigenState[0]
    eigenVectors = np.transpose(eigenState[1])
    return [eigenValues, eigenVectors] 

# print(getEigenState([[1,0,1],[0,1,0],[1,0,1]]))

# get 2D array containing all binary vectors for the given dimension as an array
# note: this does not include the zero vector or all 1s vector
def getControlSet(dim):
    result = []
    for i in range(1, (2 ** dim) - 1):
        binaryString = bin(i)[2:].rjust(dim, '0')
        binaryVector = np.array(list(binaryString)).astype(int)
        result.append(binaryVector)
    return np.array(result)

def printMatrix(matrix):
    n = np.shape(matrix)[0]
    print('')
    for i in range(n):
        row = '|'
        for j in range(n):
            value = matrix[i][j]
            if value < 0:
                row += f' {value}' # one space
            else:
                row += f'  {value}' # two spaces
        row += ' |'
        print(row)
    print('')

def zeroFloatCorrection(x):
    if abs(x) < 1e-10:
        return 0
    else:
        return x




