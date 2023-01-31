import numpy as np
import pandas as pd
import json
import pprint

import matrixGeneration
import matrixMath

data = []
dim = 7
matrixSet = matrixGeneration.getAllLaplacianMatrices(dim)

i = 1
total = np.shape(matrixSet)[0]
for matrix in matrixSet:
    print(f' evaluating matrices: {(int(i/total * 10000))/100}', end='\r')
    id = f'{dim}'.rjust(2, '0') + str(i)
    [eigenValues, eigenVectors] = matrixMath.getEigenState(matrix)
    controllability = matrixMath.pbhTest(matrix, eigenValues, eigenVectors)

    matrixString = ','.join(matrix.flatten().astype(str))
    
    data.append({
        "id": id,
        "matrix": matrixString,
        # "eigenvalues": eigenValues.tolist(),
        # "eigenvectors": eigenVectors.tolist(),
        "controllability": controllability
    })

    i += 1
print('')
print('done')
prettyPrintData = pprint.pformat(data).replace("'", '"')
# print([value for index, value in enumerate(data) if value['id'] == '05224'])
with open(f'data/data-{dim}.json', 'w') as f:
    json.dump(data, f, indent=2)

# with open('data-3.json', 'r') as f:
#     data = f.read()
#     json_data = json.loads(data)

# pprint.pprint(json_data)