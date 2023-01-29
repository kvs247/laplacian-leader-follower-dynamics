import sys
sys.path.append('../laplacian-leader-follower-dynamics')
import numpy as np
import randomMatrix

def generateRandomElementTest():
    # check that values on or below diagonal are zero
    for i in range(3, 9):
        for j in range(i, 0, -1):
            testValue = randomMatrix.generateRandomElement(i, j)
            if testValue != 0:
                raise Exception('generateRandomElementTest did not pass - nonzero element on or below diagonal')
    # check that values above diagonal are 0 or 1
    for i in range(3, 9):
        for j in range(i + 1, 9):
            testValue = randomMatrix.generateRandomElement(i, j)
            if not (testValue == 1 or testValue == 0):
                raise Exception('generateRandomElementTest did not pass - element above diagonal that is not 0 nor 1')
    print('')
    print('generateRandomElement passed')


generateRandomElementTest()

print('')
print('all tests passed')
print('')