#include "binaryVectors.h"
#include <math.h>

int *getSymmetricFlatMat(int dim, int *flatMat) {
    int *result = (int *)malloc(dim * dim * sizeof(int));
    for (int i = 0; i < dim * dim; i++) {
        if (flatMat[i] == 1) {
            int row = floor(i / dim);
            int col = i % dim;
            int transIdx = (dim * col) + row;
            result[transIdx] = 1;
            result[i] = 1;
        } else {
            if (result[i] != 1) {
                result[i] = 0;
            }
        }
    }

    return result;
}

void getLaplacianMatrices(int dim)
{
    int numElesAboveDiag = (dim / 2) * (dim - 1);
    int resultSize = (1 << (numElesAboveDiag)) - 2;
    int ***result = (int ***)malloc(resultSize * sizeof(int **));
    int **binaryVectors = getBinaryVectors(numElesAboveDiag);

    for (int i = 0; i < resultSize; i++)
    {
        int *flatMat = (int *)malloc(dim * dim * sizeof(int));
        int flatMatIdx = 0;
        int *bVector = binaryVectors[i];
        int vectorIdx = 0;
        for (int i = 1; i <= dim; i++) // iterate over matrix rows
        {
            for (int j = 0; j < dim; j++) // iterate over row elements
            {
                if (j < i)
                {
                    flatMat[flatMatIdx] = 0;
                }
                else
                {
                    flatMat[flatMatIdx] = bVector[vectorIdx];
                    vectorIdx++;
                }
                flatMatIdx++;
            }
        }
        int *symmetricFlatMat = getSymmetricFlatMat(dim, flatMat);
        printMatrix(dim, symmetricFlatMat);
    }

    // Free the binaryVectors allocated memory
    for (int i = 0; i < resultSize; i++)
    {
        free(binaryVectors[i]);
    }
    free(binaryVectors);
}

