import sys
sys.path.append('../laplacian-leader-follower-dynamics')
import numpy as np
import matrixMath

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

def getEigenStateTest():
    inputMatrix = np.array([
        [2, 0, 0],
        [1, 2, 1],
        [-1, 0, 1]
    ])
    expectedResult = np.array([2, 1, 2])
    result = matrixMath.getEigenState(inputMatrix)[0]
    if not (result == expectedResult).all():
        raise Exception('getEigenState did not pass')

getControlSetTest()
getEigenStateTest()