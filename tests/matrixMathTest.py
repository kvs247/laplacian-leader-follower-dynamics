import sys
sys.path.append('../laplacian-leader-follower-dynamics')
import numpy as np
import matrixMath


#getControlSet
def getControlSetTest():
    inputDim = 3
    expectedResult = np.array([
        [ 0, 0, 1 ],
        [ 0, 1, 0 ],
        [ 0, 1, 1 ],
        [ 1, 0, 0 ],
        [ 1, 0, 1 ],
        [ 1, 1, 0 ]
    ])
    result = matrixMath.getControlSet(inputDim)
    if not (result == expectedResult).all():
        raise Exception('getAllBinaryVectors did not pass')

getControlSetTest()