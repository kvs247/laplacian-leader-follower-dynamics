import numpy as np

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



