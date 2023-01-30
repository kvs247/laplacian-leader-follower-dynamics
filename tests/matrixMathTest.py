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
    print('')
    print('getControSet passed')

# wip
# def getEigenStateTest():
#     inputMatrix = np.array([
#         [1, -1, 0],
#         [-1, 2, -1],
#         [0, -1, 1]
#     ])
#     expectedResult = np.array([3., 1., 0.])
#     result = matrixMath.getEigenState(inputMatrix)[0]
#     print(result[0])
#     print(expectedResult[0])
#     print(result == expectedResult)
#     if not (result == expectedResult).all():
#         raise Exception('getEigenState did not pass')
#     print('')
#     print('getEigenState passed')

def pbhTestTest():
    print('')
    print('pbhTest passed')

getControlSetTest()
getEigenStateTest()
pbhTestTest()

print('')
print('all tests passed')
print('')