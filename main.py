import numpy as np
import pandas as pd
import matrixGeneration
import matrixMath

data = []
dim = 6
matrixSet = matrixGeneration.getAllLaplacianMatrices(dim)

i = 1
total = matrixSet.size
print(total)
for matrix in matrixSet:
    print(f'{i}/{total}', end='\r')
    id = f'{dim}'.rjust(2, '0') + str(i)
    [eigenValues, eigenVectors] = matrixMath.getEigenState(matrix)
    controllability = matrixMath.pbhTest(matrix, eigenValues, eigenVectors)
    
    data.append({
        "id": id,
        "matrix": matrix,
        "eigenvalues": eigenValues,
        "eigenvectors": eigenVectors,
        "controllability": controllability
    })

    i += 1

for object in data:
    if object['controllability'] == 'completely uncontrollable (nondegenerate)':
        print(object)