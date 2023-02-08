import datetime
import glob
import numpy as np
import os
import sys

import matrixGeneration
import matrixMath

controllabilityDict = {
    "essentially controllable": "EC",
    "conditionally controllable": "CC",
    "completely uncontrollable (disconnected)": "CU-dis",
    "completely uncontrollable (degenerate)": "CU-degen",
    "completely uncontrollable (nondegenerate)": "CU-nondegen"
}

def categorize(dim, directory = None):
    numMatrices = int((2 ** int((dim / 2) * (dim - 1)))) # (dim / 2) * (dim - 1) elements in matrix triangle
    matricesPerFile = 1e6  # IMPORTANT
    numFiles = int(numMatrices / matricesPerFile)
    id_dim = str(dim).rjust(2, '0')
    
    # setup starting place
    # new run
    if not directory:
        start = 0
        fileNumber = 0
        continuing = False
        # create new dir
        date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        dirpath = f'data/laplacian{dim}-{date}'
        if not os.path.exists(dirpath):
            os.mkdir(dirpath)
    # continuing run        
    else:
        files = glob.glob(f'{directory}/*.txt')
        files.sort(key = lambda x: int(os.path.basename(x).split('.')[0].split('-')[1]))
        lastFile = files[-1]
        print(" finding starting point...")
        with open(lastFile, 'r') as f:
            data = f.read()
            # recognize and process incomplete data
            # ASSUMES PROGRAM STOPPED MID FILE
            if not data.endswith(']'):
                data += ']'
            data = np.array(eval(data))
            matrixGenerators = np.array([dataObj['id'][3:] for dataObj in data]).astype(int)

            
            fileNumber = int(os.path.basename(lastFile)[:-4].split('-')[1])
            continuing = True
            dirpath = os.path.dirname(lastFile)
    
    print(" running...")
    while fileNumber <= numFiles:
        # continuing file
        if continuing:
            continuing = False
            start = np.max(matrixGenerators) + 1
            filepath = lastFile
        # new file
        else:
            start = int(fileNumber * matricesPerFile)
            filepath = f'{dirpath}/laplacian{dim}-{fileNumber}.txt'
            with open(filepath, 'a') as f:
                f.write('[')
        stop = int((fileNumber + 1) * matricesPerFile)
        # add rows
        for generator in range(start, stop):
            if generator == numMatrices:
                break

            id = f'{id_dim}{generator}'
            matrix = matrixGeneration.getLaplacianFromId(id)
            [eigenValues, eigenVectors] = matrixMath.getEigenState(matrix)
            controlClass = matrixMath.pbhTest(matrix, eigenValues, eigenVectors)

            dataObj = { 'id': f'{id[0:2]}-{id[2:]}', 'class': controllabilityDict[controlClass] }
            with open(filepath, 'a') as f:
                f.write('\n')
                f.write(str(dataObj))
                f.write(',')

        with open(filepath, 'a') as f:
            f.write('\n')
            f.write(']')

        fileNumber += 1

startTime = datetime.datetime.now()
# categorize(8, "data/laplacian8-20230206-114814")
categorize(3)
print('Done')
print(f'Execution time: {datetime.datetime.now() - startTime}')


