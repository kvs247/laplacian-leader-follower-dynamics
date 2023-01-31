import datetime
import numpy as np
import matrixGeneration
import matrixMath

def calculate(dim, filepath = None):
    numMatrices = int((2 ** int((dim / 2) * (dim - 1))) - 2) # (dim / 2) * (dim - 1) elements in matrix triangle
    id_dim = str(dim).rjust(2, '0')

    # setup starting place
    if not filepath:
        start = 1
        # create new filee
        date = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        filepath = f'data/laplacian{dim}-{date}.txt'
        with open(filepath, 'a') as f:
            f.write('[')
    else:
        with open(filepath, 'r') as f:
            data = f.read()
            # recognize and process incomplete data
            if not data.endswith(']'):
                data += ']'
            data = np.array(eval(data))

            matrixGenerators = np.array([dataObj['id'][2:] for dataObj in data]).astype(int)
            start = np.max(matrixGenerators) + 1
            if start > numMatrices:
                print('This file is complete.')
                return
            
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

    
path5 = '/home/kyle/code/laplacian-leader-follower-dynamics/data/laplacian5-20230131083831.txt'
path6 = '/home/kyle/code/laplacian-leader-follower-dynamics/data/laplacian6-20230131084518.txt'
path7 = '/home/kyle/code/laplacian-leader-follower-dynamics/data/laplacian7-20230131085525.txt'
calculate(7, path7)

