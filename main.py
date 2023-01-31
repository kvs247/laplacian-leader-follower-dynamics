import datetime
import json
import numpy as np
import matrixGeneration
import matrixMath

# dim = 3

# print(numMatrices)

def calculate(dim, filepath = None):
    numMatrices = int((2 ** int((dim / 2) * (dim - 1))) - 2) # (dim / 2) * (dim - 1) elements in matrix triangle
    id_dim = str(dim).rjust(2, '0')
    if not filepath:
        date = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        filepath = f'data/laplacian{dim}-{date}.txt'
        start = 1
        with open(filepath, 'a') as f:
            f.write('[')
    else:
        with open(filepath, 'r') as f:
            data = np.array(json.load(f))
            matrixGenerators = np.array([dataObj['id'][2:] for dataObj in data]).astype(int)
            start = np.max(matrixGenerators) + 1
            if start > numMatrices:
                print('This file is complete.')
                return
    
    # print(start)
            
    for generator in range(start, numMatrices+1):
        id = f'{id_dim}{generator}'
        matrix = matrixGeneration.getLaplacianFromId(id)
        [eigenValues, eigenVectors] = matrixMath.getEigenState(matrix)
        controlClass = matrixMath.pbhTest(matrix, eigenValues, eigenVectors)

        if controlClass == 'essentially controllable':
            dataControlClass = 'EC'
        if controlClass == 'conditionally controllable':
            dataControlClass = 'CC'
        if controlClass == 'completely uncontrollable (disconnected)':
            dataControlClass = 'CU-dis'
        if controlClass == 'completely uncontrollable (degenerate)':
            dataControlClass = 'CU-degen'
        if controlClass == 'completely uncontrollable (nondegenerate)':
            dataControlClass = 'CU-nondegen'

        dataObj = { 'id': id, 'class': dataControlClass }
        with open(filepath, 'a') as f:
            f.write('\n')
            f.write(str(dataObj))
            f.write(',')
    with open(filepath, 'a') as f:
        f.write('\n')
        f.write(']')

    

calculate(5)

