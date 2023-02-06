import datetime
import glob
import numpy as np
import os
import sys

import matrixGeneration
import matrixMath

def categorize(dim, directory = None):
    numMatrices = int((2 ** int((dim / 2) * (dim - 1)))) # (dim / 2) * (dim - 1) elements in matrix triangle
    matricesPerFile = 1e4
    numFiles = int(numMatrices / matricesPerFile)
    id_dim = str(dim).rjust(2, '0')
    

    # setup starting place
    # new run
    if not directory:
        start = 0
        thisFile = 0
        continuing = False
        # create new dir
        date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        dirpath = f'data/laplacian{dim}-{date}'
        if not os.path.exists(dirpath):
            os.mkdir(dirpath)
    # continuing run        
    else:
        pass
        # with open(filepath, 'r') as f:
        #     data = f.read()
        #     # recognize and process incomplete data
        #     if not data.endswith(']'):
        #         data += ']'
        #     data = np.array(eval(data))
        #     matrixGenerators = np.array([dataObj['id'][2:] for dataObj in data]).astype(int)

        #     start = np.max(matrixGenerators) + 1
        #     thisFile = int(os.path.basename(filepath)[:-4].split('-')[1])
        #     continuing = True
        #     dirpath = os.path.dirname(filepath)
        #     if start > numMatrices:
        #         print('This file is complete.')
        #         return
            
    while thisFile <= numFiles:
        # continuing file
        if continuing:
            continuing = False
        # new file
        else:
            start = int((thisFile) * matricesPerFile)
            stop = int((thisFile + 1) * matricesPerFile)
            filepath = f'{dirpath}/laplacian{dim}-{thisFile}.txt'
            with open(filepath, 'a') as f:
                f.write('[')
        # add rows
        for generator in range(start, stop):
            if generator == numMatrices:
                break
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

        thisFile += 1

startTime = datetime.datetime.now()
# categorize(7, "data/laplacian7-20230206-090353/laplacian7-1.txt")
categorize(6)
print('Done')
print(f'Execution time: {datetime.datetime.now() - startTime}')
